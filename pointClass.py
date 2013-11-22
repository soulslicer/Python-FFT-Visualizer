from numpy import sin, linspace, pi, fft
from pylab import plot, show, title, xlabel, ylabel, subplot
from scipy import fftpack, arange
from array import *
import matplotlib.pyplot as plt
import datetime
import time
import csv

class Point:
    def __init__(self):
        self.X=0
        self.Y=0

class PointArray:
	def __init__(self):
		self.timeArray=[]
		self.freqArray=[]

	def initArrays(self):
		self.timeArray=[]
		self.freqArray=[]

	def populateWithStream(self,stream):
		self.initArrays()

		i=0
		for elem in stream:
			point=Point()
			point.X=i
			self.timeArray.append(point)
			i+=1

		i=0
		for elem in stream:
			point=self.timeArray[i]
			if elem==0:
				point.Y=0
				self.timeArray[i]=point
			if elem==1:
				point.Y=1
				self.timeArray[i]=point
			i+=1

		n=len(stream)
		fyArr=fft.fft(stream)
		dt=60
		freqs=fft.fftfreq(n,d=dt)

		fftXArr=fft.fftshift(freqs)
		fftYArr=fft.fftshift(abs(fyArr))

		i=0
		for elem in stream:
			point=Point()
			point.X=fftXArr[i]
			point.Y=fftYArr[i]
			self.freqArray.append(point)
			i+=1

	def printTimeArrCood(self):
		i=0
		for point in self.timeArray:
			i+=1
			if i==len(self.timeArray):
				break
			print '('+str(point.X)+','+str(point.Y)+')'

	def printFreqArrCood(self):
		i=0
		for point in self.freqArray:
			i+=1
			if i==len(self.freqArray):
				break
			print '('+str(point.X)+','+str(point.Y)+')'