FRAMERATE = 0

WINDOW_SIZE = (1920, 1080)

FULLSCREEN = True


import ast
import configparser
import os
import io

if os.path.exists('spacefarer.properties'):
    _parser = configparser.ConfigParser()
    _data = '[globs]\n'
    with open('spacefarer.properties') as fp:
        _data += fp.read()
    _parser.read_string(_data, 'spacefarer.properties')
    globals().update({k.upper(): ast.literal_eval(v) for (k, v) in _parser['globs'].items()})
else:
    _parser = configparser.ConfigParser()
    _parser['globs'] = {k.lower(): repr(v) for (k, v) in globals().items() if k.isupper()}
    _data = io.StringIO()
    _parser.write(_data)
    _data.seek(8)
    with open('spacefarer.properties', 'w') as fp:
        fp.write(_data.read())

del ast, configparser, os, _parser, _data
