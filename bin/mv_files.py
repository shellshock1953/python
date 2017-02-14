import os
import datetime
import shutil

dirs =  [   "/home/shellshock/Pictures/themes/xfce/dark/",
            "/home/shellshock/",
            "/home/shellshock/Downloads/",
        ]
destination = "/home/shellshock/Pictures/themes/xfce/dark/1/"


def fullpath_mp4(dirs):
    fullpath_to_mp4 = []
    for dir in dirs:
        [fullpath_to_mp4.append(dir + file) for file in os.listdir(dir) if 'mp4' in file or 'webm' in file]
    return fullpath_to_mp4


def creation_date(file):
    raw_date = os.path.getctime(file)
    human_date = datetime.datetime.fromtimestamp(raw_date)
    return human_date


def mv_files(source, target):
    for file in source:
        timestamp = creation_date(file)
        if 'mp4' in file:
            move_to = target + str(timestamp).replace(' ', '_') + '.mp4'
        else:
            move_to = target + str(timestamp).replace(' ', '_') + '.webm'
        shutil.move(file, move_to)
        print("!! %s >>> %s") % (file, move_to)


def folder_lock(folder, lock_trigger):
    if lock_trigger == "lock":
        print(">_L0ck1nG %s") % folder
        os.chmod(folder, 0000)
    elif lock_trigger == "unlock":
        print(">_Un:0ck1nG %s") % folder
        os.chmod(folder, 0777)

if __name__ == "__main__":
    print "..>>.h1d3 F1leS..__."
    folder_lock(destination, "unlock")
    mv_files(fullpath_mp4(dirs), destination)
    folder_lock(destination, "lock")
    print "..??.AlL d0n3_^///"
