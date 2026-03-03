# Day 21 – Simple file organizer (auto-sort files by type)

import os
import shutil


def organize_folder(path):
    if not os.path.exists(path):
        print("Folder does not exist.")
        return

    for file in os.listdir(path):
        full_path = os.path.join(path, file)

        if os.path.isfile(full_path):
            ext = file.split(".")[-1]

            folder_name = ext.upper() + "_files"
            target_folder = os.path.join(path, folder_name)

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            shutil.move(full_path, os.path.join(target_folder, file))

    print("Files organized successfully.")


if __name__ == "__main__":
    folder_path = input("Enter folder path to organize: ")
    organize_folder(folder_path)