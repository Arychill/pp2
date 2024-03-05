import os

def list_directories_files(path):
    directories = []
    files = []
    all_directories_files = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            directories.append(item)
            all_directories_files.append(item)
        elif os.path.isfile(os.path.join(path, item)):
            files.append(item)
            all_directories_files.append(item)
    
    print("Directories:", directories)
    print("Files:", files)
    print("All Directories and Files:", all_directories_files)

path = '/Users/argynmoldabek/Desktop/pp2/lab6'
list_directories_files(path)

def check_access(path):
    access_info = {
        'existence': os.path.exists(path),
        'readable': os.access(path, os.R_OK),
        'writable': os.access(path, os.W_OK),
        'executable': os.access(path, os.X_OK)
    }
    return access_info

path = '/Users/argynmoldabek/Desktop/pp2/lab6/file.txt'
print(check_access(path))


def path_info(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return filename, directory
    else:
        return "Path does not exist", None

path = '/Users/argynmoldabek/Desktop/pp2/lab6/file.txt'
print(path_info(path))

def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

file_path = '/Users/argynmoldabek/Desktop/pp2/lab6/file.txt'
print("Number of lines:", count_lines(file_path))


def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

file_path = '/Users/argynmoldabek/Desktop/pp2/lab6/file.txt'
data = ['apple', 'banana', 'orange']
write_list_to_file(file_path, data)

import string

def generate_files():
    for letter in string.ascii_uppercase:
        file_name = '/Users/argynmoldabek/Desktop/pp2/lab6/' + letter + '.txt'
        with open(file_name, 'w') as file:
            pass  

generate_files()

def copy_file(source, destination):
    with open(source, 'r') as src_file:
        with open(destination, 'w') as dest_file:
            dest_file.write(src_file.read())

# Example usage
source_file = '/Users/argynmoldabek/Desktop/pp2/lab6/file.txt'
destination_file = '/Users/argynmoldabek/Desktop/pp2/lab6/A.txt'
copy_file(source_file, destination_file)

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            return "File deleted successfully"
        else:
            return "No write access to the file"
    else:
        return "File does not exist"

# Example usage
file_path = '/Users/argynmoldabek/Desktop/pp2/lab6/Z.txt'
print(delete_file(file_path))
