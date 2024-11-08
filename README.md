## nameCheck: Make your Yearbook Avenue name-checking a little easier
nameCheck is a small program that compares a class roster to a Yearbook Avenue coverage report and a High School Class roster. It will check if a name in YBA is in the class roster and, if not, add it to a list of "unverified" students. 

### Supported file formats:
Tested formats:
* .XLSX
* .XLS
Technically any file formats on [this page](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#excel-files) are supported, but they must have the correct column names seen below

### Terms used in project
* YBA - Yearbook Avenue (a Jostens product used to create yearbooks)
* PG - High School (stands for "placeholder", but I typed g and not h :/ )
* Verified - Names on both lists
* Unverified - Names on the YBA list but not the PG list.
* Untagged - Students who are verified but do not have any photos of them tagged

## How to use
Run the EXE file to create a template config file, then put paths to HS and YBA spreadsheets. 

&nbsp;&nbsp;&nbsp;***IMPORTANT***: Your spreadsheets must have all students in separate "Last Name" and "First Name" columns. They don't have to be in any specific order. Also, the spreadsheets must contain only the students from the same grade (e.g. both lists must only contain students from the 9th grade, no others). The different classes can be in different sheets inside the same file, and those separate sheets can be selected using their respective parameters in the config file (currently unimplemented for the HS list).

After the lists are in the config file, run the program. The program will complete and export the results to the `log.txt` file if the lists are set up correctly. If one doesn't exist, it will create a new one. If a log file exists, the results will be appended at the end of the file.

If for any reason your config file breaks, delete it entirely. The program will automatically create a blank file you can refill.

If you have any issues, head to https://github.com/Equalizer5118/nameCheck/issues and create an issue. If you have a desperate problem, email me at grantb1224@hotmail.com. Make sure to title your email with "[nameCheck URGENT ISSUE]: Issue Here" and I will get back to you as soon as possible. 

## Build instructions
First, you must have the following modules installed:
* pandas
* xlrd
* pyinstaller
Next, run the program from the .py file to check that you have all the required modules installed. If a config file gets successfully generated, then you have all the proper modules.

Finally, navigate to the project's root directory and run the `build.bat` batch file. The compiled EXE file will be placed in the `dist` folder. Remember to keep the _internal folder with the EXE file, or the program will not work.
