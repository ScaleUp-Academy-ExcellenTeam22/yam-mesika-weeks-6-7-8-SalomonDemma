from PIL import Image


def decrypt_image(path: str) -> str:
    """
    This function decrypts message from the image (if one exists)
    :param path: Get a path of an image encrypted.
    :return string: The decrypted message (as a string) of the encrypted message
    """
    input_image = Image.open(path)
    pixels = input_image.load()
    width, height = input_image.size
    return ''.join([chr(row) for col in range(width) for row in range(height) if pixels[col, row] == 1])


if __name__ == "__main__":
    print(decrypt_image(input("enter photo path: ")))