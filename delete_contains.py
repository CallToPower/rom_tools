import os
import sys

content = ['Alt 1', '(Alpha)', '(Beta)', '(Beta 1)', '(Beta 2)', '(Rev A)', '(Rev B)']

def delete_languages(path):
    if not os.path.isdir(path):
        print('Path "{}" is not a directory'.format(path))
        return
    for f in os.listdir(path):
        full_name = '{}/{}'.format(path, f)
        if os.path.isdir(full_name):
            delete_hidden(full_name)
        else:
            contains = False
            for c in content:
                if c in f:
                    contains = True
            if contains:
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
    delete_languages(path)
