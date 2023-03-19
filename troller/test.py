import os
import sys
import threading
import winshell
from win32com.client import Dispatch
import pythoncom
import win32com.shell.shell as shell

def add_to_startup(file_path):
    startup_folder = shell.SHGetFolderPath(0, shellcon.CSIDL_STARTUP, None, 0)
    target_path = f'"{sys.executable}" "{file_path}"'
    wDir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    shortcut = os.path.join(startup_folder, file_name + ".lnk")
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut)
    shortcut.Targetpath = target_path
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = f'{sys.executable},0'
    shortcut.Save()

# Add the Python script to startup
script_path = sys.argv[0]
add_to_startup(script_path)

# Your code to run the video goes here...

