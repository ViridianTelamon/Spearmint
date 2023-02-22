from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET"] = "0bf4e18f5ea33519601b4ed1fb77f80e"
socketio = SocketIO(app, cors_allowed_origins="*")
@socketio.on("message")
def handle_messsage(message):
    print("Received Message:  " + message)
    if message != "User Connected!":
        send(message, broadcast=True)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    socketio.run(app, host="127.0.0.1")