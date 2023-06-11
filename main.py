from PIL import Image
from flask import Flask, request, send_file
from image_functions import toPng, downloadFunction, backgroundImageRemove
import threading
import os
import time

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


def auto_delete():
    print("running the auto cleanup function")
    try:
        current_time = time.time()
        for file_name in os.listdir('./outputImages'):
            file_path = os.path.join("./outputImages", file_name)
            if current_time - os.path.getctime(file_path) > 300:
                os.remove(file_path)
                print(f"removed {file_path} successfully")
    except Exception as e:
        print(f"An error occured while auto deleting the files")

def cleanup():
    while True:
        auto_delete()
        time.sleep(300)

cleanup_thread = threading.Thread(target=cleanup)
cleanup_thread.daemon = True
cleanup_thread.start()


auto_delete()
if __name__ == "__main__":
    app.run(debug=True, port=5000)
