import os, shutil


with open("spotify_cache_path.txt") as file:
    path = file.read()
    for element in os.listdir(path):
        shutil.rmtree(os.path.join(path, element))
