import sys
import os
import numpy
import shutil

fileString = str(sys.argv[1])

rootPath = "recorder_Data/EventRecords/" + fileString + "/";
S3Path = "eventRecords/storage/" + fileString + "/";
filePath = "recorder_Data/EventRecords/" + fileString + "/Dissonance_Diagnostics/"
speechPath = "eventRecords/storage/" + fileString + "/speech/"
logPath = "eventRecords/eventLog.txt"

if not os.path.exists(speechPath):
    os.makedirs(speechPath)

shutil.copyfile(rootPath + "actions.txt", S3Path + "actions.txt")
shutil.copyfile(rootPath + "audio.txt", S3Path + "audio.txt")
shutil.copyfile(rootPath + "player.txt", S3Path + "player.txt")
shutil.copyfile(rootPath + "slideReactions.txt", S3Path + "slideReactions.txt")
shutil.copyfile(rootPath + "transforms.txt", S3Path + "transforms.txt")

for filename in os.listdir(filePath):
    trackPath = filePath + filename;
    shutil.copyfile(trackPath, speechPath + filename)

with open(logPath, 'r') as myfile:
    data=myfile.read()

f= open(logPath,"w+")
f.write(data + fileString + ",\n")
f.close()
