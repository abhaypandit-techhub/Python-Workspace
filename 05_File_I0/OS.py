import os
a=os.listdir("direc")
# Directory must be in current working file

print(a)
print(os.getcwd()) # get current working directory
print(os.path.exists("direc")) # check file exist or not in True/False term
# os.remove("sample3.txt") # delete the file in File_IO
#os.rename("infor1.txt","infor.txt")#rename the file or directory