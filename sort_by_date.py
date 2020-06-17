#! Python3
#this is a program to sort any files from any dir to new destination in creation date order.
from pathlib import Path
import os, time, glob, shutil   #TODO: import all things

# select  dir to request to sort
path_selected=Path(input('type path to sort: '))
type_of_file=input('which type of file u want to sort?: ')


# check if there are .jpg files in folder and subfolders .
files=list(path_selected.rglob('*.'+type_of_file))


# print message if there nothing to sort
numbers_of_files=len(list(files))
if numbers_of_files == 0:
    print("There's nothing to sort dude")
# take a date of creation of each files
else:
    for i in range(numbers_of_files):
        creation_time=time.ctime(os.path.getmtime(files[i]))
        month=creation_time[4:7]
        year=creation_time[-4:]
        folder=type_of_file+'/'+month+year
        # create a .dir-s from dates from jpg to sort files
        try:
            os.chdir(path_selected/folder)
        except FileNotFoundError:
            os.makedirs(path_selected/folder)
        # move files to match dir
        sciezka=Path(path_selected/folder)
        shutil.move(str(files[i]),sciezka)
