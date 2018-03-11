from PIL import Image


def get_array_from_image(image_path, width=32, height=32):
    image = Image.open(image_path)
    image = image.resize((width, height))
    image = image.convert(mode="1")
    bits = map(lambda x: '1' if x == 0 else '0', list(image.getdata()))
    return bits
