from PIL import Image


def toPng(files):
    try:
        for i, file in enumerate(files):
            image = Image.open(file)
            image.save(f"./outputImages/output{i}.png", "PNG")
        return "success"
    except Exception as e:
        return f"This is the Error: {e.args}"
