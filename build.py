from os import scandir
from zipfile import ZipFile
import PyInstaller.__main__
import src.ver as a
import sys

z = 1
b = 1
of = 0

args = sys.argv
if len(args) > 1:
    if '--nozip' in args or '-nz' in args:
        z = 0
    if '--nobuild' in args or '-nb' in args:
        b = 0
    if '--version' in args:
        i = args.index('--version')
        try:
            a.ver = args[i+1]
        except IndexError:
            print('--version missing argument, ignoring.')
    if '--onefile' in args or '-o' in args:
        of = 1

if z == 0 and b == 0:
    print('Why tf are you not building or zipping? Why are you even running this script? \n'\
          'I mean, seriously, whats the point? Ur just wasting time. In the time it took you to type out \n'\
          'the full program name AND the arguments, you could have done quite litterally anything else. \n' \
          'your mind truely is an interesting place...')
    print('Now that ur done wasting both of our time,')

if b == 1:
    print('Building program...')
    iargs = ['src\\main.spec', '-y']
    if of == 1:
        iargs.append('-F')
    PyInstaller.__main__.run(iargs)
    print('Program successfully compiled!')

if z == 1:
    print(' Zipping file...')
    list = []
    def dir_scan(path):
        for i in scandir(path):
            if i.is_file():
                list.append(str(i.path))
            elif i.is_dir():
                dir_scan(i.path)
    dir_scan('dist\\main')

    with ZipFile(f'dist\\nameCheck-{a.ver}.zip', 'w') as myzip:
        for i in list:
            myzip.write(i)

    print("All files successfully zipped!")

k = input('Press enter to close this window...')