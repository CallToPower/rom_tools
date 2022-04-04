import os
import sys

protected = ['.gitignore', '.gitattributes']
exclude_paths = ['bios-old', 'bios', 'dos', 'ports', 'doom', 'tools']

def delete_hidden(path):
    if not os.path.isdir(path):
        print('Path "{}" is not a directory'.format(path))
        return
    for f in os.listdir(path):
        full_name = '{}/{}'.format(path, f)
        if f in exclude_paths:
            # print('Excluded directory: "{}"'.format(f))
            continue
        if os.path.isdir(full_name):
            delete_hidden(full_name)
        else:
            if f[0] == '.' and not f in protected:
                try:
                    os.remove(full_name)
                    print('Removed: {}'.format(full_name))
                    pass
                except:
                    print('Could not remove: {}'.format(full_name))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = os.getcwd()
    delete_hidden(path)
