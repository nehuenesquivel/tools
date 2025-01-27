import os
import sys

with open(sys.argv[1]) as file:
    for line in file:
        process_name = line.rstrip()
        os.system(f"taskkill /f /im {process_name}")
