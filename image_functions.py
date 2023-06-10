from PIL import Image


def toPng():
    try:
        image = Image.open("./input.jpg")
        image.save("output.png", "PNG")
        return "success"
    except Exception as e:
        return f"This is the Error: {e.args}"
