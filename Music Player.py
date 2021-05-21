import pygame
from tkinter import *
import tkinter as tk
import os

# Window
player = tk.Tk()

player.title("Music Player")
window_width = 240
window_height = 400
player.geometry(f"{window_width}x{window_height}")

# Playlist Register
os.chdir(r"D:\PyCharm Community Edition 2020.3.1\PycharmProjects\Projects\Music Player\music")
print(os.getcwd())
song_list = os.listdir()

# Volume
volume_level = tk.Scale(player, from_=0.0, to_=1.0, orient=tk.HORIZONTAL, resolution=0.1)

# Playlist input
playlist = tk.Listbox(player, highlightcolor='blue', selectmode=tk.SINGLE)
print(song_list)
for song in song_list:
    pos = 0
    playlist.insert(pos, song)
    pos = pos + 1

# PyGame Inits
pygame.init()
pygame.mixer.init()

# Song name
var = tk.StringVar()
song_title = tk.Label(player, textvariable=var)


# Activate event

def play():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volume_level.get())
    print(pygame.mixer.music.get_volume())
    print(volume_level.get())


def exit_player():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


# Buttons
play_button = tk.Button(player, width=2, height=2, text="PLAY", command=play)
stop_button = tk.Button(player, width=2, height=2, text="STOP", command=exit_player)
pause_button = tk.Button(player, width=2, height=2, text="PAUSE", command=pause)
unpause_button = tk.Button(player, width=2, height=2, text="UNPAUSE", command=unpause)

# Place widgets
song_title.pack()
play_button.pack(fill="x")
stop_button.pack(fill="x")
pause_button.pack(fill="x")
unpause_button.pack(fill="x")
volume_level.pack(fill='x')
playlist.pack(fill='both', expand='yes')

# Run program
player.mainloop()
