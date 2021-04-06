from flask import Flask
import os
import socket

# Connect to Redis

app = Flask(__name__)

@app.route("/")
def hello():

    html = "<h3>Hello {name}!</h3>" \
           "<b>Parola d'ordine:</b> {paroladordine}"
    return html.format(
        name=os.getenv("NAME", "world"),
        paroladordine=os.getenv("PAROLADORDINE", "Il fosso si salta senza rincorsa e la signora cammina con la borsa")
    )

