import os
import re
import argparse

def get_files_list(files_directory_path, pattern):
    files_list = []
    for file in os.listdir(files_directory_path):
        file_extension = file.split('.')[-1]
        if re.match(pattern, file_extension):
            files_list.append(file)
    return files_list

def parse_command_line():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-p', '--path', type=str, metavar='', help='Path to directory where files are located')
    parser.add_argument('-e', '--extension',type=str, default=r'\w+', metavar='', help='File extension of desired files. regex or literal, i.e. txt, doc etc')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_command_line()
    files_list = get_files_list(args.path,args.extension)
    print(files_list)

        

