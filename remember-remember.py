from PIL import Image


def decrypt_image(path: str) -> str:
    """
    This function decrypts message from the image (if one exists)
    :param path: Get a path of an image encrypted.
    """

    input_image = Image.open(path)
    pixels = input_image.load()
    width, height = input_image.size

    massage_decrypted = ''
    for col in range(width):
        for row in range(height):
            if pixels[col, row] == 1:
                massage_decrypted.join(chr(row))

    return massage_decrypted

if __name__ == "__main__":
    print(decrypt_image(input("enter photo path: ")))
