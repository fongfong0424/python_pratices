import os
import shutil

path = "/Users/tess/Documents/KFS"
filelist = os.listdir(path)
#print(filelist)
for i in filelist:
    NewFile = i.replace("-", "_")
    print(NewFile)\


    #shutil.move(path+i, path+NewFile)