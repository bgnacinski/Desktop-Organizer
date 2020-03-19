#support libreoffice
#support microsoft office

import os

def scan_dir(dir):
    files = []
    folders = []

    for i in os.listdir(dir):
        if os.path.isfile(dir + i):
            files.append(i)

        elif os.path.isdir(dir + i):
            folders.append(i)
    return files, folders

def move_file(file, dir):
    os.system("mv {} {}".format(path + file, dir + "/" + file))

path = "/home/darkmoon/Desktop/"

files_on_desktop = []

try:
    os.mkdir(path + "pdf")
    os.mkdir(path + "txt")
    os.mkdir(path + "web")
    os.mkdir(path + "programming")

except:
    pass

files_on_desktop, x = scan_dir(path)
print("{} files will be moved".format(files_on_desktop))

for file in files_on_desktop:
    if ".txt" in file:
        move_file(file, path + "txt")
        print("[*] {} moved to txt folder".format(file))

    elif ".pdf" in file:
        move_file(file, path + "pdf")
        print("[*] {} moved to pdf folder".format(file))

    elif ".html" in file or ".php" in file or ".css" in file or ".js" in file:
        move_file(file, path + "web")
        print("[*] {} moved to web folder".format(file))

    elif ".py" in file or ".rb" in file or ".cs" in file or ".cpp" in file or ".c" in file or ".sh" in file or ".java" in file:
        move_file(file, path + "programming")
        print("[*] {} moved to programming folder".format(file))

    else:
        print("[!] {} is unsupported file type.".format(file))