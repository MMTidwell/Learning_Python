my_list = [5, 2, 1, True, 'abcdefg', 3, False, 4]

import pdb; pdb.set_trace()
#    Make sure that all of pdb is taken out when you are done. Otherwise it will hic-up when it is running

del my_list[3]  # [5, 2, 1, 'abcdefg', 3, False, 4]
del my_list[3]  # [5, 2, 1, 3, False, 4]
del my_list[4]  # [5, 2, 1, 3, 4]
print(my_list)


# This task is asking what is going on inside the broken code, in order to fix it. We are wanting to take out
#   everything but the numbers. The old way is by adding print lines after each line of code. The new one is calling
#   on pdb.set_trace(). Here is what it looks like in the terminal.

#   C:\Python27\python.exe "C:/Users/mittsy/Google Drive/TreeHouse/buggy.py"
#   > c:\users\mittsy\google drive\treehouse\buggy.py(6)<module>()
#   -> del my_list[3]
#   (Pdb) my_list ====> prints my_list
#   [5, 2, 1, True, 'abcdefg', 3, False, 4]
#   (Pdb) n ===> runs next line
#   > c:\users\mittsy\google drive\treehouse\buggy.py(7)<module>()
#   -> del my_list[3]
#   (Pdb) my_list
#   [5, 2, 1, 'abcdefg', 3, False, 4]
#   (Pdb) n
#   > c:\users\mittsy\google drive\treehouse\buggy.py(8)<module>()
#   -> del my_list[4]
#   (Pdb) my_list
#   [5, 2, 1, 3, False, 4]
#   (Pdb) n
#   > c:\users\mittsy\google drive\treehouse\buggy.py(9)<module>()
#   -> print(my_list)
#   (Pdb) my_list
#   [5, 2, 1, 3, 4]
#   (Pdb) q ===> exits sys

#   or
#   > c:\users\mittsy\google drive\treehouse\buggy.py(9)<module>()
#   -> print(my_list)
#   (Pdb) c ===> continue
#   [5, 2, 1, 3, 4]


# Other methods could be used for this such as REMOVE
