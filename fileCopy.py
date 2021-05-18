import os
import shutil

path = input("Please enter the file path.")

List_Of_Files = os.listdir(path)

print(List_Of_Files)

for file in List_Of_Files:
    splitF = os.path.splitext(file)
    ext = splitF[1]
    if (ext == " "):
        continue
    if os.path.exists(path + '/' + ext):
        shutil.copy2(path + '/' + file, path + '/' + ext)
    else:
        os.makedirs(path + '/' + ext)
        shutil.copy2(path + '/' + file, path + '/' + ext)
