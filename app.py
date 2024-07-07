from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
	return render_template('welcome.html')

@app.route('/info')
def info():
	return '<h2>Flask002</h2><p>This is the info page.</p>'

port = 3737
print(f'DEV SITE: http://localhost:{port}')
if __name__ == "__main__":
    app.run(port=port, debug=True)