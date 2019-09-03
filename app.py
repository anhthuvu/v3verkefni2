from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Flask er flottast</h1><a href="/sida1">Sida 1</a>'

@app.route('/sida1')
def sida1():
	return '<h1>HH</h1>'

if __name__ == "__main__":
	app.run(debug=True)