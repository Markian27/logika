from PIL import Image, ImageFilter

with Image.open('zaparic.jpg', 'r') as photo:
    print(photo.size)
    print(photo.format)
    print(photo.mode)
    #photo.show()

    #bl_photo = photo.convert("L")
    #bl_photo.show()

    #bl_photo = photo.filter(ImageFilter.BLUR)
    #bl_photo.show()

    left_photo = photo.transpose(Image.ROTATE_90)
    left_photo = left_photo.transpose(Image.ROTATE_90)
    left_photo.show()




