# -*- mode: python ; coding: utf-8 -*-
from shutil import copy
from pathlib import Path

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('..\\assets\\icon.ico', 'assets'), ('configcreate.py','.'), ('debugprint.py','.'), 
           ('nameCheck.py','.'), ('qt_mainwindow.py','.'), ('qt_univerr.py','.'), ('spreadsheetms.py','.'), ('writelog.py','.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='nameCheck',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon='..\\assets\\icon.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)

try:
    Path.unlink('dist\\nameCheck.zip')
except:
    pass
copy('README.md', 'dist\\main\\README.md')
copy('VERSION.md', 'dist\\main\\VERSION.md')
