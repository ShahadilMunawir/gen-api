from PIL import Image


def toPng(files, extension, quality):
    try:
        for i, file in enumerate(files):
            image = Image.open(file)
            image.save(f"./outputImages/output{i}.{extension}", f"{extension}", quality=quality)
        return "success"
    except Exception as e:
        return f"This is the Error: {e.args}"
