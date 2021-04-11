from PIL import Image
import PIL

#ascii charachter
ascii_char = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

#resize the image
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return(resize_image)

#convert colors to grey
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

#pixels to ascii
def pixels_ascii(image):
    pixels = image.getdata()
    characters = "".join([ascii_char[pixel//25] for pixel in pixels])
    return(characters)

def main(new_width=100):
    image = PIL.Image.open("shrek.jpg")
    
    new_image_info = pixels_ascii(grayify(resize_image(image)))

    pixel_count = len(new_image_info)
    ascii_image = "\n".join([new_image_info[index:(index+new_width)] for index in range(0, pixel_count, new_width)])

    print(ascii_image)


main()