cd $home
Invoke-WebRequest -Uri "https://github.com/boatinalamp/troller/raw/main/bat.zip" -OutFile "bat.zip"
Expand-Archive bat.zip -DestinationPath bat
cd bat\bat\
.\source.bat
Read-Host -Prompt "Press Enter to exit"