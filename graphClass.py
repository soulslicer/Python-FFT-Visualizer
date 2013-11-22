from numpy import sin, linspace, pi, fft
from pylab import plot, show, title, xlabel, ylabel, subplot
from scipy import fftpack, arange
from array import *
from pointClass import *
import matplotlib.pyplot as plt
import datetime
import time
import csv

class Graph:
    def __init__(self):
        self.pointArray = PointArray()
    description = "This is a class"
    author      = "Raaj"

    def setPointArray(self,pointArray):
        self.pointArray=pointArray

    def plotFFTGraph(self):
        xArr=[]
        yArr=[]
        
        for point in self.pointArray.freqArray:
            xArr.append(point.X)
            yArr.append(point.Y)

        subplot(2,1,2)
        plot(xArr,yArr)

    def plotTimeGraph(self):
        xArr=[]
        yArr=[]
        for point in self.pointArray.timeArray:
            xArr.append(point.X)
            yArr.append(point.Y)

        subplot(2,1,1)
        plt.axis([0, len(xArr), 0, 2])
        #plot(self.xArr,self.yArr,'ro')
        plot(xArr,yArr)

    def showGraphs(self):
        show()
