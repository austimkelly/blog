# Import the Flask module and create a Flask web server from the Flask module
# Also import the render_template function from the flask module
from flask import Flask, render_template

# __name__ means this current file. In this case, it will be app2.py. This current file will represent my web application.
app = Flask(__name__)

# We are using the route() decorator to tell Flask what URL should trigger our function.
# The function name is also used to generate URLs for that particular function.
@app.route('/')
def hello_world():
    # Instead of returning a string, we're returning the rendered template.
    # Flask will look for templates in the "templates" directory, and we have a file in there called index.html
    # We're also passing a variable message to our template, with the value 'Hello, World!'
    return render_template('index.html', message='Hi How Are you?!')

# Main driver function. If we're running this file directly and not importing it, only then run the app.
if __name__ == '__main__':
    # run() method of Flask class runs the application on the local development server.
    # debug=True will provide a useful debugger to track the errors if any, in the application.
    app.run(debug=True, port=5003)