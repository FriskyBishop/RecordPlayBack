import sys
import os
import numpy
import shutil

fileString = str(sys.argv[1])

logPath = "eventRecords/eventLog.txt"

with open(logPath, 'r') as myfile:
    data=myfile.read()

f= open(logPath,"w+")
f.write(data + fileString + ",\n")
f.close()
