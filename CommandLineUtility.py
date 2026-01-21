#Creating command line utility in python=A program that takes input from the command line, performs a task, and returns output.

import argparse
import os
import shutil


def organize_folder(path):
    if not os.path.isdir(path):
        print("❌ Invalid directory path")
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            ext = file.split('.')[-1]

            target_dir = os.path.join(path, ext)
            os.makedirs(target_dir, exist_ok=True)

            shutil.move(file_path, os.path.join(target_dir, file))

    print("✅ Files organized successfully")


def main():
    parser = argparse.ArgumentParser(
        description="Organize files in a directory by extension")

    parser.add_argument(
        "path",
        help="Path of the directory to organize")

    args = parser.parse_args()
    organize_folder(args.path)


if __name__ == "__main__":
    main()
