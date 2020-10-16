import os

#k = open("/Users/tess/Documents/KFS", "r+");
#k.read();


def rename():
    path = '/Users/tess/Documents/KFS';

    filelist = os.listdir(path)
    for files in filelist:
        Olddir = os.path.join(path, files);
        filename = os.path.splitext(files)[0];
        filetype = os.path.sp;splitext(files)[1];

        if filename.find('-')>=0:
            Newdir = os.path.join






