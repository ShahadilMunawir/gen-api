from PIL import Image
from flask import Flask, request, send_file
from image_functions import toPng, downloadFunction, backgroundImageRemove

app = Flask(__name__)


@app.route("/topng", methods=["POST"])
def to_png():
    if request.method == "POST":
        if "images" not in request.files:  # checking if the images form value exist in request
            return "Image not provided"

        # checking if the extension form value exist in request
        if not request.form.get("extension"):
            return "Extension no provided"
        if not request.form.get("quality"):
            return "Quality not provided"

        # getting the image from the formdata
        image = request.files.getlist("images")


        # getting the extension from the form data and trimming the unwanted space and making it capitalize to prevent errors
        extension = request.form.get("extension").strip()
        if extension == "jpg":  # converting jpg to jpeg because using jpg is not suppoted in pillow
            extension = "jpeg"

        quality = int(request.form.get("quality").strip())


        # passing the image file list and the extension to the convertion function in the image_function.py file
        return toPng(image, extension, quality)
    else:
        return "GET method is not allowed"

@app.route("/download/<path:filename>")
def download_file(filename):
    try:
        return send_file(downloadFunction(filename), as_attachment=True)
    except Exception:
        return "File not found"

@app.route("/bgremove", methods=["POST"])
def bg_remove():
    if not request.files.getlist("images"):
        return "image not provided"
    
    image = request.files.getlist("images")
    return backgroundImageRemove(image)
if __name__ == "__main__":
    app.run(debug=True, port=5000)
