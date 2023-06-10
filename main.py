from PIL import Image
from flask import Flask, request
from image_functions import toPng

app = Flask(__name__)

@app.route("/topng", methods=["POST"])
def to_png():
    if request.method == "POST":
        if "images" in request.files :
            image = request.files.getlist("images")
            return toPng(image)
        else:
            return "No image provided"
    else:
        return "GET method is not allowed"

if __name__ == "__main__":
    app.run(debug=True, port=5000)