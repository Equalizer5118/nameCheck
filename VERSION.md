## v0.3.0: Linux Support

Program has been updated to support Linux with little to no differences in appearence/function. Current packaged version is built for Ubuntu, so you may need to rebuild for other distros.

### New Featurs / changes

* Ubuntu support
* If the lists are the same, program will ask the user if they meant to use the same list before proceeding.

  * Users can check to not show the warning again. This can be undone in Preferences
* Added preferences

  * Currently only shows setting for duplicate popup, will add more later if needed
* Added support for `.ods` files

### Bugfixes

* Fixed an issue where the list of similar names persisted between checks
* Fixed debug variable not correctly being defined in `qt_adv_vars.py`

### Code/Internal Changes

* Condensed sheet loading logic to one function
* Created basic notice template in `qt_univerr.py` to reduce duplicate code
* Bumped PySide6 version 6.8 -> 6.10
* Changed os.startfile() to pyquark.filestart() for cross-platform support
* Reduced many cases of duplicate/unused code

### Known Issues

* On linux, after toggling advanced windows a couple times, the window size will revert to the previous height when the main window loses focus. (See [this issue](https://github.com/Equalizer5118/nameCheck/issues/2))
* On linux, JSON files are loaded/saved as "data\name.json" in the base directory, not in `data/` folder. Program functions identically to Windows version.

## v0.2.6

Bugfixes + refactoring

### Bugfixes

* Fixed bug where program has a heart attack due to looking at the wrong list
* Fixed results reporting the entire list of students in a sheet and not just ones in the grade, even if grade divider is set to column

### Changes

* Collapsed Save and Load buttons into one menu instead of two
* Minor code refactoring

## v0.2.5

Name similarity checking

### New Features / changes

* Program automatically checks for similarities between roster names not in YBA and unverified names (learned why this feature is important the hard way)
  * Now dumped into the log

### Code Additions

* Added comments for the variables that may be obscure

## v0.2.4

QMainWindow + better config loading

### New Features / changes

* QT loads a QMainWindow widget instead of a QWidget now, gives access to toolbars and menus
* Added menus for "File", "Window", and "Help"
  * "File" contains config loading stuffs
  * "Window" contains toggle for Advanced menus
  * "Help" Contains links to README.md and VERSION.md
* "Go" button moved to status bar of the main window, along with a new progress bar
* Can now save to and load from configs other than 'default.json'
* default location for .json files is in `data` folder, created on program start
* Advanced windows are now incorperated into the main window, thus making them no longer modal popups

### Code Additions / changes

* Separated json file loading and program variables into separate scripts
* Moved "DefWidget()" to a separate file than mainwindow
* Advanced windows no longer use the same code, and are now separated into different classes
* Moved zip deletion code and version/readme copy code to `build.py`
* `debugprint.p()` can be run without arguments
* Removed many unused imports / code

### Known bugs

* Status tips sometimes overlap with the scroll bar (especially on loading/saving)
* Status tips do not show up for all things it should

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
