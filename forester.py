import sys
import os
import numpy
import shutil

from pyAudioAnalysis import audioTrainTest as aT

fileString = str(sys.argv[1])
rescan = str(sys.argv[2])

filePath = "recorder_Data/EventRecords/" + fileString + "/Dissonance_Diagnostics/"
speechPath = "recorder_Data/EventRecords/" + fileString + "/speech/"
noisePath = "recorder_Data/EventRecords/" + fileString + "/noise/"
nothingPath = "recorder_Data/EventRecords/" + fileString + "/nothing/"
errorPath = "recorder_Data/EventRecords/" + fileString + "/error/"

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
            """shutil.move(trackPath, errorPath + filename)"""
