from flask import Flask, render_template, request, redirect, url_for
import json
import tools as t

app = Flask(__name__)

@app.route('/home')
def welcome():
	return render_template('welcome.html', currentTime = t.getCurrentDateTimeIso())

@app.route('/create-url')
def create_url():
	return render_template('create-url.html')

@app.route('/show-url', methods=['GET', 'POST'])
def show_url():
	if request.method == 'POST':
		urls = {}
		urls[request.form['code']] = {'url': request.form['url']}
		with open('data/urls.json', 'w') as url_file:
			json.dump(urls, url_file)
		return render_template('show-url.html', code=request.form['code'])
	else:
		return redirect(url_for('welcome'))

port = 3737
print(f'DEV SITE: http://localhost:{port}')
if __name__ == "__main__":
    app.run(port=port, debug=True)