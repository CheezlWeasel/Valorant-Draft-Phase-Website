import flask
from flask-socketio import *



if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port='80', debug=False)
#server communication will be run out of this file
#all flask/flask-socketio operations