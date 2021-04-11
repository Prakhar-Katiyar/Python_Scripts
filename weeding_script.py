import os
import shutil
from PIL import Image
#using argument parser for making target directory dynamic. i.e Using command promp we can run this file anywhere(on top of any folder)
import argparse

def main(Target_dir):
    #Target_dir = "Power BI"
    os.chdir(Target_dir)

    files = os.listdir(".")
    #print(files)

    os.makedirs("Trash", exist_ok=True)

    for file_ in files:
        try:
            Image.open(file_)
        except Exception as e:
            print(f"Error: {e}")
            shutil.move(file_,"Trash")
            #print(f"{file_} moved to Trash dir")
            #pass

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--target", default="Power BI")
    #more than 1 arguments can be added and evertime you run this file both the target folders will be affected parallely
    parsed_args = args.parse_args()
    print(parsed_args.target)
    main(Target_dir=parsed_args.target)
