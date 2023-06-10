from flask import Flask
from PIL import Image

app = Flask(__name__)



@app.route("/topng")
def toPng():
    try:
        image = Image.open("./input.jpg")
        image.save("output.png", "PNG")
        return "success"
    except Exception as e:
        return f"This is the error {e.args}"




if __name__ == "__main__":
    app.run(debug=True, port=3000)