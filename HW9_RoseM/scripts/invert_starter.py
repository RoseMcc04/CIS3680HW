"""
File: invert.py
Defines and tests a function for inverting images.
"""

from images import Image
import os

def invert(image: Image) -> None:
    """
    Inverts an image to its negative.
    
    Args:
        image (Image): Image we are turning into its negative.
    """
    width = image.getWidth()
    height = image.getHeight()
    for i in range(width):
        for j in range(height):
            (r, g, b) = image.getPixel(i, j)
            r  = 255 - r
            g  = 255 - g
            b  = 255 - b
            image.setPixel(i, j, (r, g, b))

def blackAndWhite(image: Image) -> None:
    """
    Converts an image to black and white.
    
    Args:
        image (Image): Image you are turning to black and white.
    """
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x, y, blackPixel)
            else:
                image.setPixel(x, y, whitePixel)

def grayscale(image: Image) -> None:
    """
    Converts an image to grayscale.
    
    Args:
        image (Image): Image you are turning to grayscale.
    """
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b) = image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x, y, (lum, lum, lum))

def main():
    filename = input("Enter the image file name: ")
    if not os.path.isfile(filename):
        print(f"The file {filename} was not found.")
        return
    else:
        print(f"The file {filename} exists.")
    
    image = Image(filename)
    
    #Invert image
    # invert(image)
    # image.draw()
    
    #Covert to greyscale, then invert
    # grayscale(image)
    # invert(image)
    # image.draw()
    
    #Convert to black and white, then invert
    # blackAndWhite(image)
    # invert(image)
    # image.draw()

if __name__ == "__main__":
   main()
