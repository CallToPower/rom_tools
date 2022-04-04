import os
import sys
import shutil

ignore_files = ['.DS_Store']

def move_ports(path):
    if not os.path.isdir(path):
        print('Path "{}" is not a directory'.format(path))
        return
    move_name = '000moved'
    move_dir = '{}/{}'.format(path, move_name)
    if not os.path.isdir(move_dir):
        try:
            os.mkdir(move_dir)
        except:
            print('Could not create move directory "{}"'.format(move_dir))
    else:
        print('Move directory "{}" already exists'.format(move_dir))
    for maindir in os.listdir(path):
        if move_name in maindir or not os.path.isdir(maindir):
            pass
        full_path = '{}/{}'.format(path, maindir)
        if os.path.isdir(full_path):
            for f in os.listdir(full_path):
                if not f in ignore_files:
                    full_name = '{}/{}'.format(full_path, f)
                    full_name_moved = '{}/{}'.format(move_dir, f)
                    try:
                        shutil.move(full_name, full_name_moved)
                        print('Moving: {} -> {}'.format(full_name, full_name_moved))
                    except:
                        print('Could not move "{}"'.format(f))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = os.getcwd()
    move_ports(path)
