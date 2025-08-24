import os
folders = input("please provide list of folder names with spaces in between:").split()

for folder in folders:
   
    try:
       files = os.listdir(folder)
    except FileNotFoundError:
       print("please provide a valid folder name, looks like the given folder does not exist:" + folder)
       continue
    except PermissionError:
       print("No access to this folder:" + folder)
    
print("list of files in the folder-" + folder)
for file_list in files:
        print(file_list)



