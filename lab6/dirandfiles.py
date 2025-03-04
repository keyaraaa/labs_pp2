import os
import string

#task1
def list_directories(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

def list_directories_and_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    
    print("Directories:", directories)
    print("Files:", files)

def files_in_specific_path(path):
    if os.path.exists(path):
        print(f"Files in {path}:")
        for item in os.listdir(path):
            if os.path.isfile(os.path.join(path, item)):
                print(item)
    else:
        print(f"Path '{path}' does not exist")

path = os.path.expanduser("~/Desktop/labs_pp2")
specificPath = os.path.expanduser("~/Desktop/my_project")

list_directories(path)
list_directories_and_files(path)
files_in_specific_path(specificPath)

#task2
def check_access(path):
    print(f"Path: {path}")
    print(f"Exists: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")

check_access(path)

#task3
def check_path_info(path):
    if os.path.exists(path):
        print(f"Path '{path}' exists")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print(f"Path '{path}' does not exist")

check_path_info(path)
check_path_info(specificPath)

#task4
def count_lines(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            print(f"Lines in {filename}: {len(file.readlines())}")
    else:
        print(f"File '{filename}' does not exist")

lines = ["Hello my future friends!\n", "My name is Beksh\n", "Byee\n"]
with open("pythonLines.txt", "w") as file:
    file.writelines(lines)

count_lines("pythonLines.txt")

#task5
my_list = ["Cake", "Apple", "Pear"]
with open("foodList.txt", "w") as file:
    file.write("\n".join(my_list))

#task6
folder = os.path.expanduser("~/Desktop/works")
os.makedirs(folder, exist_ok=True)

for letter in string.ascii_uppercase:
    filename = os.path.join(folder, f"{letter}.txt")
    with open(filename, "w") as file:
        file.write(f"This is {letter}.txt")

#task7
def copy_file(source, destination):
    if os.path.exists(source):
        with open(source, "r") as infile, open(destination, "w") as outfile:
            for line in infile:
                outfile.write(line)
        print(f"Copied '{source}' to '{destination}'")
    else:
        print(f"Source file '{source}' does not exist")

copy_file("pythonLines.txt", "copy.txt")

#task8
def delete_file(path):
    if not os.path.exists(path):
        print(f"File '{path}' does not exist")
        return
    if not os.access(path, os.W_OK):
        print("No write access to delete the file")
        return

    try:
        os.remove(path)
        print(f"Deleted: {path}")
    except Exception as e:
        print(f"Error deleting file: {e}")

delete_file("copy.txt")