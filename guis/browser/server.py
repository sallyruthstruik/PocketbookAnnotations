import logging
import multiprocessing
import os
import threading
from pathlib import Path

from flask import Flask, jsonify, request, render_template, send_file
from flask_cors import CORS

from core.controller import AnnotationsPageController
from core.data_extractor import DataExtractor
from core.utils import CustomEncoder

current_dir = Path(__file__).parent

app = Flask(__name__)
app.json_encoder = CustomEncoder
app.template_folder = os.path.abspath(current_dir/"client")
app.static_folder = os.path.abspath(current_dir/"client/dist/static")
app.static_url_path = "static"

CORS(app)

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


@app.route("/markdown/annotations")
def markdown_annotations():
    return send_file(
        controller.annotations_as_markdown(**dictargs()),
        as_attachment=True,
        attachment_filename="annotations.md",

    )


@app.route("/api/books")
def api_books():
    return jsonify(controller.books(**dictargs()))


@app.route("/node_modules/<path:filename>")
def node_modules(filename):
    return app.send_static_file(filename)


@app.route("/api/open_annotation", methods=["POST"])
def open_anno():
    OID = request.json["OID"]
    controller.view_annotation(OID)
    return "{}"


class ServerProcess(multiprocessing.Process):
    def __init__(self, port, path):
        super().__init__()
        self.port = port
        self.data_extractor_path = path

    def run(self):
        controller.data_extractor = DataExtractor.from_root(self.data_extractor_path)
        app.run("127.0.0.1", self.port, debug=False)
