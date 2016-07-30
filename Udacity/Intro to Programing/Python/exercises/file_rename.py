# File rename - os.rename(old, new)

# - get file names
# - rename each file

import os


def rename():
    """ Get names from file, then rename them """
    file_list = os.listdir(r'C:\Users\mittsy\Downloads\prank\prank')   # lists all of the files in the folder
#                          r - takes in a raw path and tells the computer not to interpret any other way
    saved_path = os.getcwd()
    print("cwd is " + saved_path)
    os.chdir(r'C:\Users\mittsy\Downloads\prank\prank')
    for file_name in file_list:
        print ('Old name - ' + file_name + '    ' + 'New name - ' + file_name.translate(None, '0123456789'))
        os.rename(file_name, file_name.translate(None, '0123456789'))


rename()