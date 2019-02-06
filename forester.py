import sys
import os
import numpy
import shutil

from pyAudioAnalysis import audioTrainTest as aT

fileString = str(sys.argv[1])
rescan = str(sys.argv[2])

rootPath = "recorder_Data/EventRecords/" + fileString + "/";
S3Path = "eventRecords/storage/" + fileString + "/";
filePath = "recorder_Data/EventRecords/" + fileString + "/Dissonance_Diagnostics/"
speechPath = "eventRecords/storage/" + fileString + "/speech/"
noisePath = "eventRecords/storage/" + fileString + "/noise/"
nothingPath = "eventRecords/storage/" + fileString + "/nothing/"
errorPath = "eventRecords/storage/" + fileString + "/error/"
logPath = "eventRecords/eventLog.txt"

if not os.path.exists(speechPath):
    os.makedirs(speechPath)
if not os.path.exists(noisePath):
    os.makedirs(noisePath)
if not os.path.exists(nothingPath):
    os.makedirs(nothingPath)
if not os.path.exists(errorPath):
    os.makedirs(errorPath)

shutil.move(rootPath + "actions.txt", S3Path + "actions.txt")
shutil.move(rootPath + "audio.txt", S3Path + "audio.txt")
shutil.move(rootPath + "player.txt", S3Path + "player.txt")
shutil.move(rootPath + "slideReactions.txt", S3Path + "slideReactions.txt")
shutil.move(rootPath + "transforms.txt", S3Path + "transforms.txt")

"""
if(rescan == "true"):
    aT.featureAndTrain(["Python/pyAudioAnalysis-master/pyAudioAnalysis/classifierData/noise","Python/pyAudioAnalysis-master/pyAudioAnalysis/classifierData/speech","Python/pyAudioAnalysis-master/pyAudioAnalysis/classifierData/nothing"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
"""
for filename in os.listdir(filePath):
    trackPath = filePath + filename;
    a = aT.fileClassification(trackPath, "svmSMtemp","svm")
    b = a[1]
    if(type(b) == numpy.ndarray):
        noise = b[0]
        speech = b[1]
        nothing = b[2]
        if(speech > noise and speech > nothing):
            shutil.move(trackPath, speechPath + filename)
        if(noise > speech and noise > nothing):
            shutil.move(trackPath, noisePath + filename)
        if(nothing > speech and nothing > noise):
            shutil.move(trackPath, nothingPath + filename)
    if(type(b) != numpy.ndarray):
            shutil.move(trackPath, errorPath + filename)


with open(logPath, "a") as myfile:
    myfile.write(fileString + "\n")
