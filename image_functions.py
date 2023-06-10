from PIL import Image
from flask import Request, Response


def toPng():
    if Request.method == "POST":
        try:
            image = Image.open("./input.jpg")
            image.save("output.png", "PNG")
            return "success"
        except Exception as e:
            return f"This is the Error: {e.args}"
    else:
        return "GET method not allowed"
