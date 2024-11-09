# v0.1.1
## Bugfixes
* Config generation now happens before input prompt
* Fixed untagged image detection
* Proper handling of non-existent lists or sheet names

## New Features/Changes
* You can now select a different sheet inside the PG spreadsheet.
* (bad) Icon!
* .spec file
* `build.bat` has been improved:
    * Added -y to pyinstaller command, so it will not prompt the user to say yes to overriding the files.
    * Added Powershell command to automatically compress files to a zip
    * Now points to .spec file, so README and VERSION files get put inside `dist` automatically
* New `version.md` file to show changelogs of current and previous versions

# v0.1.0

## Features

* Compare names in two separate Excel spreadsheets
* Choose what sheet in the file to use for the YBA list (PG list not functional)
* Export to `log.txt`. Will create a new file if not found, and will append it if already exists.

## Known issues

* Exceptions created by improper lists are not properly handled
* Config file generates only after pressing enter when prompted
* "Any key" is not any key, only enter proceeds.
