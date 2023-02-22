"""    
    Copyright (C) 2023 ViridianTelamon (Viridian)
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

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
