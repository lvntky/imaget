from PIL import Image
from PIL import ImageFile
from PIL import ImageOps

def convert():
    image = input("Enter the image's name: ")
    desicion = input("Enter the file type that you want to convert: ")

    if(desicion == "jpg"):
        img = Image.open(image)
        rgb_img = img.convert('RGB')
        rgb_img.save(image + "_converted2jpg.jpg")
        print("Succesfully converted to jpg!")

    elif(desicion == "png"):
        img = Image.open(image)
        rgb_img = img.convert('RGB')
        rgb_img.save(image + "_converted2png.png")
        print("Succesfully converted to png!")

    elif(desicion == "jpeg"):
        img = Image.open(image)
        rgb_img = img.convert('RGB')
        rgb_img.save(image + "_converted2jpeg.jpeg")
        print("Succesfully converted to jpeg!")
    else:
        print("Error occured while converting...")

def resize():
    image_resize = input("Enter the image's name: ")
    suffixes = (".jpg", ".jpeg", ".png")
    
    if(image_resize.endswith(suffixes)):
        img_res = Image.open(image_resize)
        
        width = int(input('Enter width: '))
        height = int(input('Enter height: '))

        size = width, height

        img_res = img_res.resize(size, Image.ANTIALIAS)

        img_res.save(image_resize + "_resized.jpg")
        print("Succesfully resized!")
    
    else:
        print("Error occured while resizeing. Wrong file or file format...")

def flip():
    image_flip = input("Enter the image's name: ")
    suffixes = (".jpg", ".jpeg", ".png")

    if(image_flip.endswith(suffixes)):
        img_flp = Image.open(image_flip)
        
        img_flp = ImageOps.flip(img_flp)
        img_flp.save(image_flip + "_flipped.jpg")
        
        print("Succesfully flipped!")
    else:
        print("Error occured while resizeing. Wrong file or file format...")

def crop():
    imgage_crop = input("Enter the image's name: ")
    suffixes = (".jpg", ".jpeg", ".png")

    if(imgage_crop.endswith(suffixes)):
        img_crp = Image.open(imgage_crop)

        border = int(input("Enter the border for croping process: "))

        img_crp = ImageOps.crop(img_crp, border)

        img_crp.save(imgage_crop + "cropped.jpg")

        print("Successfully cropped!")
    else:
        print("Error occured while resizeing. Wrong file or file format...")

def rotate():
    image_rotate = input("Enter the image's name: ")
    suffixes = (".jpg", ".jpeg", ".png")

    if(image_rotate.endswith(suffixes)):
        img_rot = Image.open(image_rotate)

        rotateSize = int(input("Enter the rotate size: "))

        img_rot = img_rot.rotate(rotateSize)

        img_rot.save(image_rotate + "_rotated.jpg")

# Driver

desc = 0
while desc != 6:
    
    print("\nSelect Process")
    print('\n1. convert image')
    print('2. resize image')
    print('3. flip image')
    print('4. crop')
    print('5. rotate')
    print('6. exit')

    desc = int(input('\n> '))

    if(desc == 1):
        convert()
    elif(desc == 2):
        resize()
    elif(desc == 3):
        flip()
    elif(desc == 4):
        crop()
    elif(desc == 5):
        rotate()
    else:
        print('Wrong input...')