import image_gen
import ai_image_journal.image_journal.gDrive as gDrive
from dotenv import load_dotenv
import os


img = image_gen.img_gen()

gDrive.upload_image('D:\Projects\AI Image Journal\img.png', 'img.png', os.getenv("GDRIVE_FOLDER_ID") )