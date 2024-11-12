from os import scandir
from zipfile import ZipFile
import PyInstaller.__main__

PyInstaller.__main__.run([
    'src\\main.spec',
    '-y'
])

print('Program successfully compiled! Zipping file...')

list = []
def dir_scan(path):
    for i in scandir(path):
        if i.is_file():
            list.append(str(i.path))
        elif i.is_dir():
            dir_scan(i.path)
dir_scan('dist\\main')

with ZipFile('dist\\nameCheck.zip', 'w') as myzip:
    for i in list:
        myzip.write(i)

k = input('All files successfully zipped! \n Press enter to close this window...')