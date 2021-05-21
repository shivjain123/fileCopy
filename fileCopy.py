import shutil

sorucePath = input("Please enter the source path.")
destinationPath = input("Please enter destination path.")

shutil.copy2(sorucePath, destinationPath)
