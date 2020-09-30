import os
import time
import pandas

while True:
    if os.path.exists("Files/vegetables.txt"):
        with open("Files/vegetables.txt") as file:
            print(file.read())
    else:
        print('File does not exits')
    time.sleep(10)