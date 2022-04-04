import os
import sys
import shutil

endswith = ['j']

def delete_folder_endswith(path):
    if not os.path.isdir(path):
        print('Path "{}" is not a directory'.format(path))
        return
    for f in os.listdir(path):
        full_name = '{}/{}'.format(path, f)
        if os.path.isdir(full_name):
            for e in endswith:
                if f.endswith(e):
                    try:
                        shutil.rmtree(full_name)
                        print('Removed: {}'.format(f))
                    except OSError as e:
                        print('Error for "{}": %s - %s.'.format(f, e))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = os.getcwd()
    delete_folder_endswith(path)
