from PIL import Image

#given colors
dark_blue = (0, 51, 76)
light_blue = (112, 150, 158)
red = (217, 26, 33)
yellow = (252, 227, 166)

#old image manipulation
my_im = Image.open("cat.jpg")
im_list = my_im.getdata()
im_list = list(im_list)


#recoloring
recolor = []
for pixel in im_list:
    #find intensity
    intensity = pixel[0] + pixel[1] + pixel[2]
    #compare intensity to given colors
    if intensity < 183:
        pixel = dark_blue
    elif intensity > 182 and intensity < 365:
        pixel = red
    elif intensity > 364 and intensity < 547:
        pixel = light_blue
    elif intensity > 546:
        pixel = yellow;
    #assign new color to pixel
    recolor.append(pixel)

#making recoloring into new image
new_im = Image.new("RGB", my_im.size)
new_im.putdata(recolor)
new_im.show()
new_im.save("recolor.jpg", "jpeg")
