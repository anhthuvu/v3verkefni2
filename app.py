from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<nav><a href="/">Home</a><a> </a><a href="/about">About</a><a> </a><a href="/blog">Blog</a><a> </a><a href="/staff">Staff</a></nav><h1>Hello World!</h1>'

@app.route('/about')
def about():
	return '<nav><a href="/">Home</a><a> </a><a href="/about">About</a><a> </a><a href="/blog">Blog</a><a> </a><a href="/staff">Staff</a></nav><h1>About page</h1><code>This page tell you a little bit about me</code>'

@app.route('/blog')
def blog():
	return '<nav><a href="/">Home</a><a> </a><a href="/about">About</a><a> </a><a href="/blog">Blog</a><a> </a><a href="/staff">Staff</a></nav><h1>Lastest Post</h1><ul><li><h2>Kiwifruit</h2></li><li><h2>Bananas</h2></li><li><h2>Apples</h2></li></ul>'

@app.route('/staff')
def staff():
	return '<nav><a href="/">Home</a><a> </a><a href="/about">About</a><a> </a><a href="/blog">Blog</a><a> </a><a href="/staff">Staff</a></nav><h1>Staff</h1><ul><li><h2>Jill Smith</h2><h3>Chief Editor</h3></li><li><h2>Ted Doe</h2><h3>Writer</h3></li></ul>'

if __name__ == "__main__":
	app.run(debug=True)