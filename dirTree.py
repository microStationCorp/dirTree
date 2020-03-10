import os
import sys

BASE_DIR = ''


def pre_str_design(dirPath):
    str = ''
    while BASE_DIR != dirPath:
        if (len(os.listdir(os.path.dirname(dirPath))) - 1) == os.listdir(os.path.dirname(dirPath)).index(
                os.path.basename(dirPath)):
            str = '\t'  + str
        else:
            str = pipe + '\t' + str
        dirPath = os.path.dirname(dirPath)

    return str


def list_print(dir_path):
    for d in os.listdir(dir_path):
        pre_str = pre_str_design(os.path.join(dir_path))
        if (len(os.listdir(dir_path)) - 1) == os.listdir(dir_path).index(d):
            print(pre_str.expandtabs(5) + angle + dash, d)
        else:
            print(pre_str.expandtabs(5) + pipe_dash + dash, d)
        if os.path.isdir(os.path.join(dir_path, d)):
            list_print(os.path.join(dir_path, d))


argument = sys.argv[1:]
pipe = '\u2502'
pipe_dash = '\u251C'
angle = '\u2514'
dash = '\u2574'
tab = '\t'
if len(argument) != 1:
    print("give only one argument")
else:
    if argument[0] == '.':
        print(os.path.basename(os.getcwd()))
        BASE_DIR = os.getcwd()
        list_print(os.getcwd())
    else:
        files = os.listdir(".")
        try:
            index = files.index(argument[0])
            test_dir = os.path.join(os.getcwd(), argument[0])
            print(os.path.basename(test_dir))
            BASE_DIR = test_dir
            list_print(test_dir)
        except:
            print('not in this folder')
