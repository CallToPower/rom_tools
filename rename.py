#!/usr/bin/python

import sys
import os

def rename_rom(path, f):
    suffix = f[f.rfind('.'):]
    newname = f
    do_rename = False

    if ' (' in f:
        newname = '{}{}'.format(newname[:newname.index(' (')], suffix)
        do_rename = True

    if len(newname) > 3 and newname[3] == ' ':
        try:
            space_index = newname.index(' ')
            nbr = int(newname[:space_index])
            newname = newname[space_index + 1:]
            do_rename = True
        except:
            pass

    if len(newname) > 3 and newname[3] == '.':
        try:
            space_index = newname.index('.')
            nbr = int(newname[:space_index])
            newname = newname[space_index + 1:]
            do_rename = True
        except:
            pass

    if newname[0] == ' ':
        newname = newname[1:]
        do_rename = True

    if do_rename:
        os.rename('{}/{}'.format(path, f), '{}/{}'.format(path, newname))
        return '{}'.format(newname)
    else:
        return f

def rename(path):
    if not os.path.isdir(path):
        print('Path "{}" is not a directory'.format(path))
        return
    for f in os.listdir(path):
        print('{} -> {}'.format(f, rename_rom(path, f)))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = os.getcwd()
    print('Set path to "{}"'.format(path))
    rename(path)
