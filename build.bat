py -m PyInstaller src\nameCheck.spec -y
powershell Compress-Archive -Path dist\nameCheck\* -DestinationPath dist\nameCheck.zip
pause