__author__ = 'spotapov'
import os
def rename_files():
    file_list = os.listdir(r"D:\Udacity\prank")
    saved_path = os.getcwd()
    os.chdir("D:\Udacity\prank")
    #print(file_list)
    for file_name in file_list:
        a=os.rename(file_name, file_name.translate(None,"abcdfg"))
        print(file_name +" has been renamed to " +str(a))
    os.chdir(saved_path)
rename_files()