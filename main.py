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

    # libreoffice

    os.mkdir(path + "libreoffice")
    os.mkdir(path + "libreoffice/writer")
    os.mkdir(path + "libreoffice/calc")
    os.mkdir(path + "libreoffice/impress")
    os.mkdir(path + "libreoffice/draw")
    os.mkdir(path + "libreoffice/base")

except:
    pass

files_on_desktop, x = scan_dir(path)
print("{} files will be moved".format(files_on_desktop))

for filename in files_on_desktop:
    if ".txt" in filename:
        move_file(filename, path + "txt")
        print("[*] {} moved to txt folder".format(filename))

    elif ".pdf" in filename:
        move_file(filename, path + "pdf")
        print("[*] {} moved to pdf folder".format(filename))

    elif ".html" in filename or ".php" in filename or ".css" in filename or ".js" in filename:
        move_file(filename, path + "web")
        print("[*] {} moved to web folder".format(filename))

    elif ".py" in filename or ".rb" in filename or ".cs" in filename or ".cpp" in filename or ".c" in filename or ".sh" in filename or ".java" in filename:
        move_file(filename, path + "programming")
        print("[*] {} moved to programming folder".format(filename))

    #libreoffice

    elif ".odt" in filename:
        move_file(filename, path + "libreoffice/writer")
        print("[*] {} moved to writer folder".format(filename))

    elif ".ods" in filename:
        move_file(filename, path + "libreoffice/calc")
        print("[*] {} moved to calc folder".format(filename))

    elif ".odb" in filename:
        move_file(filename, path + "libreoffice/base")
        print("[*] {} moved to base folder".format(filename))

    elif ".odg" in filename:
        move_file(filename, path + "libreoffice/draw")
        print("[*] {} moved to draw folder".format(filename))

    elif ".odp" in filename:
        move_file(filename, path + "libreoffice/impress")
        print("[*] {} moved to impress folder".format(filename))

    else:
        print("[!] {} is unsupported filename type.".format(filename))