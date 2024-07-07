from flask import Flask, render_template, request
import tools as t

app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template('welcome.html', currentTime = t.getCurrentDateTimeIso())

@app.route('/create-url')
def create_url():
	return render_template('create-url.html')

@app.route('/show-url', methods=['GET', 'POST'])
def show_url():
	if request.method == 'POST':
		return render_template('show-url.html', code=request.form['code'])
	else:
		return 'not valid'

port = 3737
print(f'DEV SITE: http://localhost:{port}')
if __name__ == "__main__":
    app.run(port=port, debug=True)