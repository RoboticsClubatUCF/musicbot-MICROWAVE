from ast import In
import glob
import os
from typing import List

path = "./songs/"


class Song:
    def __init__(self, dir="") -> None:
        self.dir = dir
        self.name = self.resolve_song_name(self.dir)

    def __str__(self):
        return f"Song({self.name}, {self.dir})"

    def __repr__(self):
        return f"Song(name='{self.name}', dir={self.dir})"

    def resolve_song_name(self, s):
        if os.name == "nt":
            return s[s.find("\\", 3) + 1 : -4]
        else:
            return s[s.find("/", 3) + 1 : -4]


def get_songs():
    songlist = []
    print(os.name)
    songs = glob.glob(path + "*.mid")
    for s in songs:
        songlist.append(Song(s))
    return songlist


def get_song_request():
    songs = get_songs()
    i = 0
    for s in songs:
        print(i , " : " , s.name)
        i += 1
    choice = input("Please enter the number of any song : ")
    return songs[int(choice)]


