import multiprocessing
import os

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

from core.controller import AnnotationsPageController
from core.utils import CustomEncoder

app = Flask(__name__)
app.json_encoder = CustomEncoder
app.template_folder = os.path.abspath("guis/browser/client")
app.static_folder = os.path.abspath("guis/browser/client/dist/static")
app.static_url_path = "static"

CORS(app)

print(app.template_folder)

controller = AnnotationsPageController()


def dictargs():
    return {
        k: v
        for k, v in request.args.items()
    }


@app.route("/")
def index():
    return render_template("dist/index.html")


@app.route("/api/annotations")
def api_annotations():
    return jsonify(controller.annotations(**dictargs()))


@app.route("/api/books")
def api_books():
    return jsonify(controller.books(**dictargs()))


@app.route("/node_modules/<path:filename>")
def node_modules(filename):
    return app.send_static_file(filename)


class ServerProcess(multiprocessing.Process):
    def run(self):
        app.run("127.0.0.1", 5000, debug=True)
