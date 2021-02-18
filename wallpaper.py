import os
import shutil
from PIL import Image
import time
from datetime import datetime

# path = os.getcwd()        # current directory
# os.chdir()                # change directory - requires arguments
# print(path)

user_folder = input("HINT: User Name is folder name of your User in C:/Users/\nEnter User Name: ")
original_path = fr"C:\Users\{user_folder}\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
target_path = fr"C:\Users\{user_folder}\Desktop\wallpaper"
##final_path = r"D:\Wallpapers"

def copy_files(fn, o_p, t_p):
    if fn == 'tree':
        if os.path.isdir(t_p):
            print("TRUE!")
            for file in os.listdir(o_p):
                file_name = os.path.join(original_path, file)
                print("Copying Files...")
                shutil.copy(file_name, t_p)
        else:
            print("Copying Tree...")
            shutil.copytree(o_p, t_p)
    elif fn == 'file':
        print("Copying File to %s" % t_p)
        shutil.copy(o_p, t_p)
    else:
        print("Something is Missing in your arguments")

def change_extension(ext='.jpg'):
    for file in os.listdir(target_path):
        try:
            print("Changing extension of file '%s' to '%s' ..." % (file, ext))
            file_name = os.path.join(target_path, file)
            base = os.path.splitext(file)[0]
            os.chdir(target_path)
            os.rename(file_name, base + ext)
##        time.sleep(0.5)
        except OSError or FileExistsError:
            print("File Probably Exists")
            os.remove(file_name)
            print("Unwanted File Removed!")

def get_pixels(file_path):
    width, height = Image.open(file_path).size
    return width, height

def final_copy():
    for file in os.listdir(target_path):
        file_name = os.path.join(target_path, file)
        # print("file name: '%s': " % file, get_pixels(file_name))
        w, h = get_pixels(file_name)
        if w != 1920:
            os.remove(file_name)
            print(f"{file}: Not Require - Deleted!")
##        if w == 1920:
##            copy_files('file', file_name, final_path)
##            print("Wallpaper Copied!")
##        time.sleep(0.5)

##def old_file_check():
##    today = datetime.today()
##    for file in os.listdir(final_path):
##        modified_date = datetime.fromtimestamp(os.path.getmtime(r"D:\Wallpapers\%s" % file))
##        duration = today - modified_date
##        if(duration.days > 365):
##            os.remove(f"D:\Wallpapers\{file}")
##            print(f"{duration.days} days old file deleted: {file}")

try:
    copy_files('tree', original_path, target_path)
    change_extension('.jpg')
    final_copy()
    os.system("pause")
##    time.sleep(5)

##    print("Deleting not required folders/files")
##    old_file_check()
##    time.sleep(5)
##    shutil.rmtree(target_path, ignore_errors=True)
except FileExistsError as e:
    print("Error occured: ", e)
