import os, shutil, sys

with open(sys.argv[1]) as file:
    for line in file:
        path = line.rstrip()
        for element in os.listdir(path):
            shutil.rmtree(os.path.join(path, element))
        print(path + " cleaned")
