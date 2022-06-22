import os

def RemoveFile(File_Path):
    if os.path.exists(File_Path):
        os.remove(File_Path)
    else:
        print("Can not delete the file as it doesn't exists")