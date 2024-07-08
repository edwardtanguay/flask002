from flask import Flask, flash, render_template, request, redirect, url_for
import json
import tools as t
import os.path

app = Flask(__name__)
app.secret_key = "ksjdfwief834sjdf"

@app.route('/home')
def welcome():
	return render_template('welcome.html', currentTime = t.getCurrentDateTimeIso())

@app.route('/create-url')
def create_url():
	return render_template('create-url.html')

@app.route('/show-url', methods=['GET', 'POST'])
def show_url():
	if request.method == 'POST':
		pathAndFileName = 'data/urls.json'
		code = request.form['code']
		url = request.form['url']
		urls = {}

		if os.path.exists(pathAndFileName):
			with open(pathAndFileName) as urls_file:
				urls = json.load(urls_file)

		if code in urls.keys():
			flash(f"The key {code} already exists. Please choose another.")
			return redirect(url_for('welcome'))

		urls[code] = {'url': url}
		with open(pathAndFileName, 'w') as url_file:
			json.dump(urls, url_file)
		return render_template('show-url.html', code=code)
	else:
		return redirect(url_for('welcome'))

port = 3737
print(f'DEV SITE: http://localhost:{port}')
if __name__ == "__main__":
    app.run(port=port, debug=True)