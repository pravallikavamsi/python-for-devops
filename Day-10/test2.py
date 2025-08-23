import os
def files_list(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"
    
def main():
    folders = input("Enter a list of folders that seperated by spaces:").split ()
    for folder in folders:
        files, error = files_list(folder)
        if files:
            print(f"files in {folder}:")
            for file in files:
                print(file)
        else:
            print(f"error in {folder} folder : {error}")

if __name__ == "__main__":
    main()
