import MySQLdb

class SQL:
    def __init__(self):
        self.db=None
    description = "This is a class"
    author      = "Raaj"

    def connectToSQLServer(self):
    	self.db=MySQLdb.connect(host="",
    							user="",
    							passwd="",
    							db="")

    def runQuery(self,query):
    	print query
    	arr=[]
    	cur=self.db.cursor()
    	cur.execute(query)
    	for row in cur.fetchall():
    		arr.append(row)
    		print row
    	return arr