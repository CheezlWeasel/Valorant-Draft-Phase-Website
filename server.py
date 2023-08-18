from flask import *
from flask_socketio import SocketIO, emit
from lobby import *
lobbies = []

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app, async_mode="eventlet")

@app.route("/")
def main():
    return render_template("[PLACEHOLDER]")

@app.route("/create")
def create():
    return render_template("[PLACEHOLDER]")



@socketio.on('/create_lobby')
def create_lobby():
    lobbies.append(Lobby(session['id']))
    socketio.emit('updated_lobbies', lobbies, broadcast=True)

for i in range(len(lobbies)):
  @socketio.on(f'/{lobbies[i].code}')
  def lobby():
      return render_template("[PLACEHOLDER]", lobby = lobbies[i])
  
if __name__ == '__server__':
    socketio.run(app, host='0.0.0.0', port='80', debug=False)
#server communication will be run out of this file
#all flask/flask-socketio operations