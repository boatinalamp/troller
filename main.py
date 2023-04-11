import subprocess
from os.path import expanduser
home = expanduser("~")


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

os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.realpath(__file__))





FilePath = home+"\\.bin\\troller-main\\troll in suit.mp4"
def play_video():
    #media part
    mouse_listener = pynput.mouse.Listener(suppress=True)
    keyboard_listener = pynput.keyboard.Listener(suppress=True)
    mouse_listener = pynput.mouse.Listener(suppress=True)
    keyboard_listener = pynput.keyboard.Listener(suppress=True)
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


# run the code
th1 = threading.Thread(target=play_video)
th1.start()



