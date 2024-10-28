import image_gen
import gDrive


img = image_gen.img_gen()

gDrive.upload_image('D:\Projects\AI Image Journal\img.png', 'img.png')