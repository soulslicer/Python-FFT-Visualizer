from array import *
import datetime
import calendar
import time
import csv

class FileWriter:
    def __init__(self):
        self.unprocessedFile=""

    description = "This is a class"
    author      = "Raaj"

    def loadCSVIntoStreams(self):
        try:
            file =open(self.unprocessedFile,"r")
        except:
            print "couldn't find CSV File"

        fileContents=file.read()
        file.close()
        fileSplitByNewLine=fileContents.split("\r")
        fileSplitByComma=[elem.split(',') for elem in fileSplitByNewLine]
        activityStream=[]

        for elem in fileSplitByComma:
            activityStream.append((datetime.datetime.strptime(elem[0], "%m/%d/%y %H:%M"), datetime.datetime.strptime(elem[1], "%m/%d/%y %H:%M")))
        return activityStream

    def loadStreamFromArray(self,array):
        activityStream=[]
        for elem in array:
            activityStream.append((datetime.datetime.strptime(elem[0], "%m/%d/%y %H:%M"), datetime.datetime.strptime(elem[1], "%m/%d/%y %H:%M")))
        return activityStream;

    def getDateWithoutTime(self,firstDate):
        yearStr=str(firstDate.year)[2]+str(firstDate.year)[3]
        monthStr=str(firstDate.month)
        dayStr=str(firstDate.day)
        firstDateString=monthStr+"/"+dayStr+"/"+yearStr+" "+"00:00"
        firstDate=datetime.datetime.strptime(firstDateString, "%m/%d/%y %H:%M")
        return firstDate

    def countWalkInBooleanStream2(self,stream):
        #Get First Date without time
        firstDate=stream[0][0];
        firstDate=self.getDateWithoutTime(firstDate)
        unixFirstDate=calendar.timegm(firstDate.utctimetuple())
        #print firstDate

        #initialize unixDataStreamArray with 0's
        unixDataStreamArr=[]
        lastDate=stream[len(stream)-1][1]
        unixLastDate=calendar.timegm(lastDate.utctimetuple())
        unixLastDate=unixLastDate+86400
        lastDate=datetime.datetime.utcfromtimestamp(unixLastDate)
        lastDate=self.getDateWithoutTime(lastDate)
        unixLastDate=calendar.timegm(lastDate.utctimetuple())-unixFirstDate

        for num in range(0,unixLastDate):
            unixDataStreamArr.append(0)
        #print len(unixDataStreamArr)

        #Loop through actual stream (in seconds) (170219)
        for date in stream:
            startTimeStampUnix=calendar.timegm(date[0].utctimetuple())-unixFirstDate
            endTimeStampUnix=calendar.timegm(date[1].utctimetuple())-unixFirstDate

            for num in range(startTimeStampUnix,endTimeStampUnix+1):
                unixDataStreamArr[num-1]=1

        return unixDataStreamArr
        #for i in range(1, 4):
        #    unixDataStreamArr.extend(unixDataStreamArr)
        #return unixDataStreamArr
        # for elem in unixDataStreamArr:
        #     print elem


    def countWalkInBooleanStream(self,stream):
        refTime=stream[0][0]
        bStream=[]
        i=0
        while refTime <= stream[-1][1]:
            if stream[i][0] <= refTime and stream[i][1] >= refTime:
                bStream.append(1)
                refTime=refTime+datetime.timedelta(minutes=1)
            elif refTime > stream[i][1]:
                i+=1
            else:
                bStream.append(0)
                refTime=refTime+datetime.timedelta(minutes=1)
        return bStream

    def getProcessedStreamArrayFromUnprocessedFile(self,unprocessedFile):
        self.unprocessedFile=unprocessedFile
        astream=self.loadCSVIntoStreams()
        bstream=self.countWalkInBooleanStream2(astream)

        #self.countWalkInBooleanStream2(astream)

        return bstream

    def getProcessedStreamArrayFromArray(self,array):
        astream=self.loadStreamFromArray(array)
        bstream=self.countWalkInBooleanStream2(astream)
        return bstream

    def getProcessedStreamFromProcessedFile(self,processedFile):
        try:
            file = open(processedFile, "r")
        except:
            print "couldn't find processed file"

        fileContents = file.read()
        file.close()
        fileSplitByNewline = fileContents.split("\r")
        processedStream = []
        for elem in fileSplitByNewline:
            numElem=int(elem)
            processedStream.append(numElem)

        return processedStream
