from flask import Flask, render_template
import tools as t

app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template('welcome.html', currentTime = t.getCurrentDateTimeIso())

@app.route('/url')
def info():
	return render_template('url.html')

port = 3737
print(f'DEV SITE: http://localhost:{port}')
if __name__ == "__main__":
    app.run(port=port, debug=True)