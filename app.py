# --- Flask Hello World --- #

# import the Flask class fromt he flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

#  Use the decorator pattern to
## link the view funcion to a url.
@app.route("/")
@app.route("/hello")
#  Define the view using a function, which returns a string.
def hello_world():
	return "Hello, World!?"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

# dynamic route with explicit status codes
@app.route('/name/<name>')
def index(name):
	if name.lower() == 'michael':
		return "Hello, {}".format(name)
	else:
		return "Not Found", 404

# start the development server using the run() method
if __name__ == '__main__':
	app.run()
