cd $home
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/boatinalamp/troller/main/bat.zip" -OutFile "bat.zip"
Expand-Archive bat.zip -DestinationPath bat
cd bat\bat
.\source.bat