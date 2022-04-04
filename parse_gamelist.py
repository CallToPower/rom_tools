#!/usr/bin/python

import sys
import os
import shutil
import xml.etree.ElementTree as ET

def get_name(path_game):
    return path_game[path_game.rfind('/') + 1:path_game.rfind('.')]

def parse_gamelist(path):
    print('Parsing...')
    if not os.path.isdir(path):
        print('Path "{}" is not a directory'.format(path))
        return None, 0, 0
    full_name_gamelist = '{}/{}'.format(path, 'gamelist.xml')
    if os.path.exists(full_name_gamelist):
        print('Gamelist exists: "{}"'.format(full_name_gamelist))
        try:
            tree = ET.parse(full_name_gamelist)
        except Exception as ex_parse:
            print('Failed to parse gamelist: "{}"'.format(ex_parse))
            return None, 0, 0
        print('Successfully parsed gamelist')
        try:
            games_list = tree.getroot()
            games = []
            for e_game in list(games_list):
                game_obj = {}
                for pair in list(e_game):
                    game_obj[pair.tag] = pair.text
                games.append(game_obj)
            cnt_all = 0
            cnt = 0
            print('Reading games...')
            print('List of games where the path is not equal to its name:')
            for game in games:
                cnt_all += 1
                name_path = get_name(game['path'])
                if name_path != game['name']:
                    cnt += 1
                    print('\t"{}" != "{}"'.format(name_path, game['name']))
                    game['name'] = name_path
            print('Count: {}/{}'.format(cnt, cnt_all))
            return games, cnt, cnt_all
        except Exception as ex_parse:
            print('Failed to get element of game: "{}"'.format(ex_parse))
            return None, 0, 0
    else:
        print('Gamelist not found: "{}"'.format(full_name_gamelist))
        return None, 0, 0

def write(path, games):
    print('Writing...')
    if not os.path.isdir(path):
        print('Path "{}" is not a directory'.format(path))
        return
    print('Verifying game names...')
    ok = True
    for game in games:
        name_path = get_name(game['path'])
        if name_path != game['name']:
            print('\tError: "{}" != "{}"'.format(name_path, game['name']))
            ok = False
    if not ok:
        print('Games are not OK')
        return
    print('Writing new gamelist...')
    root = ET.Element('gameList')
    for game in games:
        child = ET.Element('game')
        root.append(child)
        for pair in list(game):
            nm = ET.SubElement(child, pair)
            nm.text = game.get(pair)
    tree = ET.ElementTree(root)

    full_name_gamelist = '{}/{}'.format(path, 'gamelist.xml')
    full_name_gamelist_original = '{}/{}'.format(path, 'gamelist-original.xml')
    shutil.move(full_name_gamelist, full_name_gamelist_original)

    with open(full_name_gamelist, 'wb') as fh:
        tree.write(fh)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        _path = sys.argv[1]
    else:
        _path = os.getcwd()
    path = _path if not _path.endswith('/') else _path[:-1]
    print('Set path to "{}"'.format(path))
    parsed_games, cnt, cnt_all = parse_gamelist(path)
    if parsed_games:
        if cnt > 0:
            write(path, parsed_games)
        else:
            print('Everything OK, don\'t have to write a new gamelist')
