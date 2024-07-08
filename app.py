from flask import Flask, flash, render_template, request, redirect, url_for
import json
import tools as t
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "ksjdfwief834sjdf"

@app.route('/')
def welcome():
	return render_template('welcome.html', currentTime = t.getCurrentDateTimeIso())


@app.route('/info')
def info():
	emp = {
		"firstName": "Sangee",
		"age": 34
	}
	colors = ["red", "blue"]
	return render_template('info.html', emp = emp, colors = colors)


@app.route('/create-url')
def create_url():
	return render_template('create-url.html')

@app.route('/show-url', methods=['GET', 'POST'])
def show_url():
	if request.method == 'POST':
		pathAndFileName = 'data/urls.json'
		code = request.form['code']
		urls = {}

		if os.path.exists(pathAndFileName):
			with open(pathAndFileName) as urls_file:
				urls = json.load(urls_file)

		if code in urls.keys():
			flash(f"The key {code} already exists. Please choose another.")
			return redirect(url_for('create_url'))

		if 'url' in request.form.keys():
			url = request.form['url']
			urls[code] = {'url': url}
		else:
			f = request.files['file']
			uploadPathAndFileName = code + secure_filename(f.filename)
			f.save(uploadPathAndFileName)
			urls[code] = {'file': uploadPathAndFileName}


		with open(pathAndFileName, 'w') as url_file:
			json.dump(urls, url_file, indent=4)
		return render_template('show-url.html', code=code)
	else:
		return redirect(url_for('welcome'))

port = 3737
print(f'DEV SITE: http://localhost:{port}')
if __name__ == "__main__":
    app.run(port=port, debug=True)