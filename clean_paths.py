import os, shutil


with open("D:/github/tools/cache_paths.txt") as file:
    for line in file:
        path = line.rstrip()
        for element in os.listdir(path):
            shutil.rmtree(os.path.join(path, element))
        print(path + " cleaned")