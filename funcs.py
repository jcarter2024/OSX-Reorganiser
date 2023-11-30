import os
from os.path import *
import subprocess

#functions 
def filename_adjust(filename):
    """ os.rename cannot overwrite. This causes gaps. ensure that no filename is made of only numbers"""
    pre=filename.strip('.jpeg')
    if pre.isdigit()==True:
        new= pre+'h.jpeg'
        os.rename(filename, new)
        print('changed', filename, 'to', new, 'to avoid rewrite errors later')

        
def onboard_filenames(img_dir1):
    """ load filenames into a list (onlyfiles) <- os friendly
        duplicate list with backslash before spaces (onlyfilesnospace) <- bash friendly 
    """
    onlyfiles = [f for f in os.listdir(img_dir1) if isfile(join(img_dir1, f))]

    #rename files that have only a number in the name 
    for filename in onlyfiles:
        filename_adjust(filename)

    onlyfiles = [f for f in os.listdir(img_dir1) if isfile(join(img_dir1, f))]

    if '.DS_Store' in onlyfiles:
        onlyfiles.remove('.DS_Store')

    #iterate through file names to place a forward slash before space or mdls wont work 
    onlyfilesnospace = []
    for i in range(len(onlyfiles)):
        tempstr = onlyfiles[i]
        if ' ' in tempstr:
            name  = tempstr.split()
            name2 = '\ '.join(map(str, name))
            onlyfilesnospace.append(name2)
        else:
            onlyfilesnospace.append(tempstr)

    print("there are "+str(len(onlyfiles))+" files in this directory")
    return onlyfiles, onlyfilesnospace


        
def date_it(fn, dr):
    """ put in filename, get out date from Content created field 
    """
    lines = []
    string = "mdls " +dr+fn
    this   = subprocess.Popen(string, shell=True, stdout=subprocess.PIPE) 
    
    for line in this.stdout.readlines():
        lines.append(str(line))
    for line in lines:
        if 'ContentCreationDate ' in line:
            A = str(line.split()[2]) #year month
            B = str(line.split()[3]) #mins secs
            date= (A+' '+B)
    return date 



def sort_namedate(onlyfiles, onlyfilesnospace, img_dir):
    """create a dictionary that associates file name with date 
    """
    
    images, n = {}, 0
    for i in range(len(onlyfiles)):
#         print(n)
        images[onlyfiles[i]] = date_it(onlyfilesnospace[i], img_dir)
        n+=1
    return images


def rename_files(sorted_list):
    """Takes time ordered list of filenames, renames to number order"""
    print('Number of files before:', len(subprocess.Popen('ls ', shell=True, stdout=subprocess.PIPE).stdout.readlines()))
    counter = 1
    for pair in sorted_list:
        nm, ext = pair[0].split('.')
        print('renaming', pair[0], pair[1], 'to', str(counter)+'.'+ext)
        os.rename(pair[0], str(counter)+'.'+ext)
        counter+=1
    print('Number of files after:', len(subprocess.Popen('ls ', shell=True, stdout=subprocess.PIPE).stdout.readlines()))
    print("Process Complete")