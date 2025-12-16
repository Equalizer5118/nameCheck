## nameCheck: Make your Yearbook Avenue name-checking a little easier

nameCheck is a small program that compares a class roster to a Yearbook Avenue coverage report and a High School Class roster. It will check if a name in YBA is in the class roster and, if not, add it to a list of "unverified" students.

### Supported file formats:

Generally, any file format supported by the Pandas library should work. These formats have been tested and work:

* .XLSX
* .XLS
* .ods (Open Document Format)

### Terms used in project

* YBA - Yearbook Avenue (a Jostens product used to create yearbooks)
* PG - High School (stands for "placeholder", but I typed g and not h and got too lazy to fix)
* Verified - Names on both lists
* Unverified - Names on the YBA list but not the PG list.
* Untagged - Students who are verified but do not have any photos of them tagged

## How to use

Run the EXE file to open the nameCheck GUI. Click the open buttons to select your spreadsheets and then type the sheet name to use for each list into their respective boxes.

&nbsp;&nbsp;&nbsp;***IMPORTANT***: Your spreadsheets must have all students in separate "Last Name" and "First Name" columns. They don't have to be in any specific order. Also, the spreadsheets must contain only the students from the same grade (e.g. both lists must only contain students from the 9th grade, no others). The different classes can be in different sheets inside the same file, and those separate sheets can be selected using their respective parameters in the GUI.

After your lists and sheet names are in the correct boxes, toggle whether or not to generate a log (recommended to toggle on) and click "Go!". The program will report when it has completed with a popup giving the basic results of the comparison. More comprehensive data will be outputted to a log file (named "log.txt") if you choose to generate one.

If you have any issues, head to https://github.com/Equalizer5118/nameCheck/issues and create an issue. If you have a desperate problem, email me at grantb1224@hotmail.com. Make sure to title your email with "[nameCheck URGENT ISSUE]: Issue Here" and I will get back to you as soon as possible.

## Build instructions

Make sure you have at least Python V3.12.x installed on your machine. Create a [Python Virtual Environment (venv)](https://python.land/virtual-environments/virtualenv) in the same directory as the source code. Activate it and then run this command:

```
py -m pip install -r requirements.txt
```

This will install all the dependencies needed to run the program. After all the requirements are installed, run `build.py` to build and zip the program. The program will be located in the `dist` folder.
