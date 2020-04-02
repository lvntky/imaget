from PIL import Image
from PIL import ImageFile

def convert():
    image = input("Enter the image's path: ")
    desicion = input("Enter the file type that you want to convert: ")

    if(desicion == "jpg"):
        img = Image.open(image)
        rgb_img = img.convert('RGB')
        rgb_img.save(image + "_converted2jpg.jpg")

    elif(desicion == "png"):
        img = Image.open(image)
        rgb_img = img.convert('RGB')
        rgb_img.save(image + "_converted2png.png")

    elif(desicion == "jpeg"):
        img = Image.open(image)
        rgb_img = img.convert('RGB')
        rgb_img.save(image + "_converted2jpeg.jpeg")

 
    



convert()