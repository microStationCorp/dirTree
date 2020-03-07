import os
import sys


def list_print(dir_path, child_num=0):
    tab_value = child_num * 5 + 1
    str = "\t|"
    print(str.expandtabs(tab_value))
    for d in os.listdir(dir_path):
        path_str = "\t|--> " + d
        print(path_str.expandtabs(tab_value))
        if os.path.isdir(os.path.join(dir_path, d)):
            list_print(os.path.join(dir_path, d), child_num + 1)


argument = sys.argv[1:]
if len(argument) != 1:
    print("give only one argument")
else:
    if argument[0] == '.':
        print(os.path.basename(os.getcwd()))
        list_print(os.getcwd())
    elif argument[0]=="..":
        print(os.path.basename(os.path.dirname(os.getcwd())))
        list_print(os.path.dirname(os.getcwd()))
    else:
        files = os.listdir(".")
        try:
            index = files.index(argument[0])
            test_dir = os.path.join(os.getcwd(), argument[0])
            print(os.path.basename(test_dir))
            list_print(test_dir)
        except:
            print('not in this folder')
# print(os.path.basename(test_dir))
# list_print(test_dir)
