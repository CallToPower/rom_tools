import os
import sys

exclude_paths_rf = ['bios-old', 'bios', 'dos', 'ports', 'doom', 'tools']
exclude_files_d = ['images', 'gamelist.xml']

def get_filenames_in(path):
    image_names = []
    if not os.path.isdir(path):
        print('Path "{}" is not a directory'.format(path))
        return []
    for f in os.listdir(path):
        image_names.append(f)
    return image_names

def list_newpreviews(path):
    if not os.path.isdir(path):
        print('Path "{}" is not a directory'.format(path))
        return
    # list rom folders folder
    for rf in os.listdir(path):
        if rf in exclude_paths_rf:
            continue
        full_path_rf = '{}{}'.format(path, rf)
        if os.path.isdir(full_path_rf):
            image_names = []
            full_path_images = '{}/{}'.format(full_path_rf, 'images')
            if os.path.exists(full_path_images) and os.path.isdir(full_path_images):
                image_names = get_filenames_in(full_path_images)
                print('Checking roms in "{}"'.format(full_path_rf))
                # list individual rom folder
                for d in os.listdir(full_path_rf):
                    if not d in exclude_files_d:
                        full_path_d = '{}/{}'.format(full_path_rf, d)
                        for r in os.listdir(full_path_d):
                            full_path_r = '{}/{}'.format(full_path_d, r)
                            if not os.path.isdir(full_path_r):
                                romname = r[:r.index('.')]
                                found = False
                                for iname in image_names:
                                    if iname.startswith(romname):
                                        found = True
                                if found:
                                    #print('Found: "{}" - "{}"'.format(romname, full_path_r))
                                    pass
                                if not found:
                                    print('Not found: "{}" - "{}"'.format(romname, full_path_r))
                                    pass
                print('')
            else:
                print('Image directory does not exist: "{}"'.format(full_path_images))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        path = os.getcwd()
    list_newpreviews(path)
