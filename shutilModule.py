#shutil Module in python=Its a module that provides a higher level interface for working with file and directories.The name "shutil" is short of shell utility.
#It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories.The syntax is:import shutil.
#Functions:-
#1.shutil.copy(src,dst):This function copies the file located at src to a new location specified by dst.If the destination location already exists,the original file will be overwritten.
#2.shutil.copy2(src,dst):This function is similar to shutil.copy,but it also preserves more metadata about the original file,such as timestamp.
#3.shutil.copytree(src,dst):This function recursively copies the directory located at src to a new location specified by dst.If the destination location already exists,the original directory will be merged with it.
#shutil.move(src,dst):This function moves the file located at src to a new location specified by dst.This function is equivalent to renaming a file in most cases.
#shutil.rmtree(path):This function recursively deletes the directory located at path,along with all of its contents.This function is similar to using rm-rf command in a shell.

import shutil
import os

if os.path.exists("main.py"):
    shutil.copy("main.py", "main2.py")
else:
    print("main.py does not exist")

if os.path.isdir(".tutorial"):
    shutil.copytree(".tutorial", "mytutorial", dirs_exist_ok=True)

    src = ".tutorial/file.file"
    if os.path.exists(src):
        shutil.move(src, "file.file")
else:
    print(".tutorial folder missing")

if os.path.isdir("mytutorial"):
    shutil.rmtree("mytutorial")

if os.path.exists("file.file"):
    os.remove("file.file")
