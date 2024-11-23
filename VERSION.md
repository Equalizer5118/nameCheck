## v0.2.3
Small bugfix + code improvements
### Additions
* Pass `-v` or `--version` to the program to see the version number

### Bugfixes
* Fixed program saying "press any key to exit" on startup (aka me being an idiot)
* Changed `except Exception` to `except BaseException`

### Code Additions
* Version stored in `ver.py`, stores version used during build process
* `build.py` improvements:
  * Passing `--nozip` or `-nz` will now prevent a zip file from being generated
  * Passing `--nobuild` or `-nb` will prevent PyInstaller from rebuilding the program
  * Passing `--onefile` or `-of` will now build the program into one file (not tested, should work)
  * Passing `--version version_number_here` (NOT `-v`) will give a custom version number to put on the zip file (note: does not currently change the number in ver.py, so the program will still show the version number in there when passing `-v` to the executable)
* `main.spec` will now report if the zip file it is trying to delete is not there instead of just passing the exception

## v0.2.2
### New Features/changes
* Added advanced options for each path, so you can now specify custom First name and last name columns, as well as the ability to filter students by a specific column value.
* Settings are now saved to a .json file (named `default.json`), which is saved when you exit the program. This is also loaded automatically, if it exists, on program load.
* Better handling of exceptions on program load, so even school computers that won't let you use CMD can see the stupid mistakes I make!
* Variables used by modules are stored in `qt_adv_vars.py`
* Icon now shows on QT window!

### Known bugs
* Console reports that its unable to set directory to "." on first open of file dialog. Not really a bug,just annoying. Program works fine and doesn't break, properly set after closing file dialog again.

## v0.2.1

### Bugfixes

* Attempted to fix random exception on program start. Works, but IDK how :/

## v0.2.0

### New Features/ changes

* Added GUI based on QT (from PySide6 module)
* Better handling of errors thanks to QT.
  * Will now display a popup displaying the exception, and will print the full traceback to console
* Passing "--debug" or "-d" will print more information to the console for debugging purposes (handled by src/debugprint.py)

### Bugfixes

* Fixed console spitting out the tagged pages for EVERY student in YBA (now debug print)

### Code improvements

* Split all the large functions into modules, so the code looks much cleaner (aside from the large amount of comments. Placeholders for CLI implementation)
* Replaced most of the `print()` commands are replaced by `debugprint.p()`, so random debug print statements will not be spit out in the console.
* build.bat has been replaced with build.py, so different platforms can now run the same command (not just windows)
* Added `requirements.txt`, which marks all the required python modules needed. Run `python -m pip install requirements.txt` to install.

### Known Bugs

* (Technically not a but, just not implemented) No data saved in-between launches; Have to retype everything on relaunch
* Putting anything, even invalid lists, in the textboxes will allow nameCheck to be ran. Causes exceptions due to invalid spreadsheets/sheetnames

## v0.1.1

### Bugfixes

* Config generation now happens before input prompt
* Fixed untagged image detection
* Proper handling of non-existent lists or sheet names

### New Features/Changes

* You can now select a different sheet inside the PG spreadsheet.
* (bad) Icon!
* .spec file
* `build.bat` has been improved:
  * Added -y to pyinstaller command, so it will not prompt the user to say yes to overriding the files.
  * Added Powershell command to automatically compress files to a zip
  * Now points to .spec file, so README and VERSION files get put inside `dist` automatically
* New `version.md` file to show changelogs of current and previous versions

## v0.1.0

### Features

* Compare names in two separate Excel spreadsheets
* Choose what sheet in the file to use for the YBA list (PG list not functional)
* Export to `log.txt`. Will create a new file if not found, and will append it if already exists.

### Known issues

* Exceptions created by improper lists are not properly handled
* Config file generates only after pressing enter when prompted
* "Any key" is not any key, only enter proceeds.
