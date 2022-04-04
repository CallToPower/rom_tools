import os
import sys
import shutil

def move_to_alphabet_folders(path):
    if not os.path.isdir(path):
        print('Path "{}" is not a directory'.format(path))
        return
    for f in os.listdir(path):
        full_name = '{}/{}'.format(path, f)
        if os.path.isdir(full_name):
            print('Ignoring directory "{}"'.format(full_name))
        else:
            try:
                first_char = f[0].upper()
                folder_name = '{}/{}'.format(path, first_char)
                if os.path.exists(folder_name) and os.path.isdir(folder_name):
                    full_name_moved = '{}/{}'.format(folder_name, f)
                    try:
                        shutil.move(full_name, full_name_moved)
                        print('Moving: {} -> {}'.format(full_name, full_name_moved))
                    except:
                        print('Failed to move {}'.format(f))
                else:
                    print('Folder does not exists: {}'.format(first_char))
            except:
                print('Could not find correct folder for {}'.format(f))
                pass

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = os.getcwd()
    move_to_alphabet_folders(path)
