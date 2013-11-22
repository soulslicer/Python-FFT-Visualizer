from graphClass import Graph
from fileClass import FileWriter
from pointClass import *
from sqlClass import SQL

fileWriter=FileWriter()
pointArray=PointArray()
graph=Graph()
sql=SQL()

# stream=fileWriter.getProcessedStreamArrayFromArray(arr)
stream=fileWriter.getProcessedStreamArrayFromUnprocessedFile("samplefile.csv")
pointArray.populateWithStream(stream)
pointArray.printTimeArrCood()
graph.setPointArray(pointArray)
graph.plotTimeGraph()
graph.plotFFTGraph()
graph.showGraphs()