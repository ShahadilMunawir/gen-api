from PIL import Image
from flask import Flask, request
from image_functions import toPng

app = Flask(__name__)

@app.route("/topng")
def to_png():
    if request.method == "GET":
        return toPng()

if __name__ == "__main__":
    app.run(debug=True, port=5000)