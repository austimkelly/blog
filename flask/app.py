# Import the Flask module and create a Flask web server from the Flask module
from flask import Flask
# __name__ means this current file. In this case, it will be app.py. This current file will represent my web application.
app = Flask(__name__)

# We are using the route() decorator to tell Flask what URL should trigger our function.
# The function name is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.
@app.route('/foo')
def hello_world():
    return 'Hello, World!'

# Main driver function. If we're running this file directly and not importing it, only then run the app.
if __name__ == '__main__':
    # run() method of Flask class runs the application on the local development server.
    # debug=True will provide a useful debugger to track the errors if any, in the application.
    app.run(debug=True, port=5003)
