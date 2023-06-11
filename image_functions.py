from PIL import Image
import os


def toPng(files, extension, quality):
    try:
        download_file_list = []
        for i, file in enumerate(files):
            image = Image.open(file)
            image.save(f"./outputImages/output{i}.{extension}", f"{extension}", quality=quality)
            download_file_list.append(f"http://localhost:5000/download/output{i}.{extension}")
        return download_file_list
    except Exception as e:
        return f"This is the Error: {e.args}"


def downloadFunction(filename):
    try:
        file_path = os.path.join("./outputImages", filename)
        return file_path
    except Exception:
        return "File not found"
