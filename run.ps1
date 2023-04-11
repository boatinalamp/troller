Set-location -Path $HOME
cmd /C curl "https://codeload.github.com/boatinalamp/troller/zip/refs/heads/main" --output main.zip
cmd /C tar xf .\main.zip
Set-location -Path troller-main





