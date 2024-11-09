py -m PyInstaller nameCheck.spec -y
powershell Compress-Archive -Path dist\nameCheck\* -DestinationPath dist\nameCheck.zip
pause