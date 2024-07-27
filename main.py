from PIL import Image, ImageFilter

#open an image file
image = Image.open(r"path")

new_size = (200, 100)
image = image.resize(new_size, Image.LANCZOS)

image = image.convert('L')
pixels = image.load()
width, height = image.size

with open(r"path to txt file", 'w') as log_file:
    for y in range(height):
        for x in range(width):
            pixel_value = pixels[x, y]

            if pixel_value < 32:
                log_file.write(".")
            elif pixel_value < 64:
                log_file.write(":")
            elif pixel_value < 96:
                log_file.write("-")
            elif pixel_value < 128:
                log_file.write("=")
            elif pixel_value < 160:
                log_file.write("+")
            elif pixel_value < 192:
                log_file.write("*")
            elif pixel_value < 224:
                log_file.write("&")
            else:
                log_file.write("#")

        log_file.write("\n")

