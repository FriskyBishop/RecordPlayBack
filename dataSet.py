import sys
import os
import numpy
import shutil

from pyAudioAnalysis import audioTrainTest as aT
aT.featureAndTrain(["Python/pyAudioAnalysis-master/pyAudioAnalysis/classifierData/noise","Python/pyAudioAnalysis-master/pyAudioAnalysis/classifierData/speech","Python/pyAudioAnalysis-master/pyAudioAnalysis/classifierData/nothing"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
