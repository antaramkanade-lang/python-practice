# Clear the Clutter =write a program to clear a clutter inside the folder on your computer.You should use os module to rename all the png images from 1.png all the way till n.png where n is no. of png files of that folder.

import os #here using os is important because without os we cannot rename,delete files or see folders or read directory contents

data_folder = os.path.join(os.getcwd(), "data") #this os.path.join is used to “Join path pieces using the correct OS rules.” and os.getcwd() used to tell “Where is my Python program currently running from?”

png_files = [f for f in os.listdir(data_folder) if f.lower().endswith(".png")]

for i, file in enumerate(png_files, start=1): #enumerate is use to print each item and its index at the same time
    old_path = os.path.join(data_folder, file)
    new_path = os.path.join(data_folder, f"{i}.png")
    os.rename(old_path, new_path)
