import re
import Image
import os

#origin_dir_name = r'C:\project\thesis\Thesis\figs_origin';
dir_name = r"C:\project\thesis\Thesis\figs";
for (dirpath, dirnames, filenames) in os.walk(dir_name):
    os.chdir(dirpath)
    #print dirpath,dirnames,filenames
    print os.getcwd()
    for file_name in filenames:
        if file_name[-3:] == 'png' or file_name[-3:] == 'jpg':
            print file_name
            full_file_name = dirpath + '\\' + file_name
            im_origin = Image.open(full_file_name)
            sz = im_origin.size
            if sz[0] == 0 or sz[1] == 0:
                continue
            sz_small = [0,0]
            sz_small[0] = sz[0]
            sz_small[1] = sz[1]
            while sz_small[0] > 300:
                sz_small[0] = sz_small[0] / 2
                sz_small[1] = sz_small[1] / 2
            im1 = im_origin.resize(sz_small)
            print im_origin
            print im1
            im1.save(full_file_name)
