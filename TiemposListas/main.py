from flask import Flask
from flask import jsonify
from linkextractor import extract_links

app = Flask(__name__)

@app.route("/")
def index():
    return "Usage: http://<hostname>[:<prt>]/api/<id>"

@app.route("/api/<int:id>")
def api(id):
    links = extract_links(50)
    links = [links[id]]
    return jsonify(links)

app.run(host="0.0.0.0")
