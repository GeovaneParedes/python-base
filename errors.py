#!/usr/bin/env python3

import sys
import os

if os.path.exists("names.txt"):
    input(...) #Race condition to check if the file exists
    names = open("names.txt").readlines()
if len(names) >= 3:
    print("Error: The file does not contain enough names.",names[2])
else:
    print("Error: The file 'names.txt' does not exist.")
    sys.exit(1)
if len(names) >= 3:
    print(names[2])
else:
    print("[Error]. Missing name in the list.")
    sys.exit(1)