cd $home
Invoke-WebRequest -Uri "https://codeload.github.com/boatinalamp/troller/zip/refs/heads/main" -OutFile "bat.zip"
Expand-Archive bat.zip -DestinationPath bat
cd bat\troller-main
python.exe main.py