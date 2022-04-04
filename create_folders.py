import os
import sys

alphabet = '#ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def create_folder(path, c):
    print(c)
    os.mkdir('{}/{}'.format(path, c))

def create_folders(path):
    if not os.path.isdir(path):
        print('Path "{}" is not a directory'.format(path))
        return
    for c in alphabet:
        create_folder(path, c)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = os.getcwd()
    create_folders(path)
