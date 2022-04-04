import os
import sys

languages = ['USA', 'Europe', 'World', 'Germany']

def delete_languages(path):
    if not os.path.isdir(path):
        print('Path "{}" is not a directory'.format(path))
        return
    for f in os.listdir(path):
        full_name = '{}/{}'.format(path, f)
        if os.path.isdir(full_name):
            delete_hidden(full_name)
        else:
            contains_lang = False
            for lang in languages:
                if lang in f:
                    contains_lang = True
            if not contains_lang:
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
