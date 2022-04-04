import os
import sys

def delete_duplicatelangs(path):
    if not os.path.isdir(path):
        print('Path "{}" is not a directory'.format(path))
        return
    list_names = []
    for f in os.listdir(path):
        if ' (' in f and 'USA' in f:
            name_clean = f[:f.index(' (')]
            list_names.append(name_clean)
    for f in os.listdir(path):
        if ' (' in f:
            name_clean = f[:f.index(' (')]
            if name_clean in list_names and not 'USA' in f:
                full_name = '{}/{}'.format(path, f)
                try:
                    os.remove(full_name)
                    print('Removed: {}'.format(full_name))
                except:
                    pass

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = os.getcwd()
    delete_duplicatelangs(path)
