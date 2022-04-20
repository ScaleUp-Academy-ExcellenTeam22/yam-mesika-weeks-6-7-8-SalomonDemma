from PIL import Image


def decrypt_image(path: str):
    """
    This function decrypted message from the image (if exit one)
    :param path: Get a path of a image encrypted.
    """
    # importing PIL
    img = Image.open(path)
    pixels = img.load()
    width, height = img.size
    for col in range(width):
        for row in range(height):
            if pixels[col, row] == 1:
                print(chr(row), end='')


if __name__ == "__main__":
    decrypt_image(input("enter photo path: "))
