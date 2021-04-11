import os
import shutil

TARGET = "Power BI"
os.chdir(TARGET)

# print(os.getcwd())

fileNames = os.listdir(".")

for file_ in fileNames:
    dirName = file_.split(".")[-1]
    os.makedirs(dirName, exist_ok = True)
    src = file_
    dst = os.path.join(dirName, file_)
    if file_ != dirName:
        #print(src,dst)
        shutil.move(src, dst)