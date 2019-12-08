#!/usr/bin/python3

import sys
import os
from datetime import datetime
from datetime import timedelta
def clean_downloads(path):
    list_files = os.listdir(path)
    strToPrint = "cleanup old files: (more than 10 days + 50MB)"
    filesToDel = []
    for aFile in list_files:
        if os.stat(path+aFile).st_size > 1000000:
            filesToDel.append(aFile)
            continue
        dateOfFile = datetime.fromtimestamp(os.stat(path+aFile).st_mtime)
        tenDayOfDiff = (datetime.now())+timedelta(days=-10)
        if dateOfFile < tenDayOfDiff:
            filesToDel.append(aFile)
            continue
    if len(filesToDel) > 0:
        print(strToPrint)
        for aFileToDel in filesToDel:
            print(aFileToDel)
    return filesToDel
    
if __name__ == "__main__":
    print(clean_downloads(sys.argv[1]))