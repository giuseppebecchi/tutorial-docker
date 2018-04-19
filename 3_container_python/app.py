from flask import Flask
import os
import socket

# Connect to Redis

app = Flask(__name__)

@app.route("/")
def hello():

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Parola d'ordine:</b> {paroladordine}"
    return html.format(
        name=os.getenv("NAME", "world"),
        hostname=socket.gethostname(),
        paroladordine=os.getenv("PAROLADORDINE", "Il fosso si salta senza rincorsa e la signora cammina con la borsa")
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)