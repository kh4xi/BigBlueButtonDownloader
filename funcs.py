import requests
from moviepy.editor import *
from datetime import datetime
import uuid
import os
from os import system, name


class MyColors:
    r_color = '\033[91m'
    g_colr = '\033[32m'
    y_colr = '\033[33m'
    n_colr = '\033[0m'


def webcams(arg_url):
    try:
        response = requests.get(arg_url + '/video/webcams.mp4', stream=True)
        with open("raw/webcams.mp3", 'wb') as f:
            f.write(response.content)
    except requests.exceptions.ConnectionError as e:
        print("Please check the link or internet connection !")


def desk_share(arg_url):
    try:
        response = requests.get(arg_url + '/deskshare/deskshare.mp4', stream=True)
        with open("raw/deskshare.mp4", 'wb') as f:
            f.write(response.content)
    except requests.exceptions.ConnectionError as e:
        print("Please check the link or internet connection !")


def mix_clips():
    try:
        videoclip = VideoFileClip("raw/deskshare.mp4")
        audioclip = AudioFileClip("raw/webcams.mp3")
        new_audioclip = CompositeAudioClip([audioclip])
        videoclip.audio = new_audioclip
        timestamp = '{}{:-%Y%m%d%H%M%S}.mp4'.format(str(uuid.uuid4().hex), datetime.now())
        videoclip.write_videofile("output/" + timestamp)
    except OSError as e:
        print("Error: %s : %s" % e.strerror)


def clean_raw():
    try:
        os.remove("raw/deskshare.mp4")
        os.remove("raw/webcams.mp3")
    except OSError as e:
        print("Error: %s : %s" % e.strerror)


def folder_integrity():
    if not os.path.exists('raw'):
        os.makedirs('raw')
    if not os.path.exists('output'):
        os.makedirs('output')
    current = os.getcwd()
    directory = os.listdir(current)
    for item in directory:
        if item.endswith(".mp3") or item.endswith(".mp4"):
            os.remove(os.path.join(current, item))
    pass


def term_clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
