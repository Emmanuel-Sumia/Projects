"""
TOOTER PROGRAM BY EMMANUEL JOHN SUMIA
"""




'''
class user:
	def __init__(self,handle,name,pin,following):
		self.handle = handle
		self.name = name	
		self.pin = pin
		self.following = following
	def getPin(self):
		
		thisDict = dict(zip(pin,handle))
		user = input("Enter your pin:")
		
		for i in thisDict:
			if user == i:
				print(thisDict.get(i))
									#name = []
									#pin = []
				handle = []
				date = []
									#following = []
				message = []
				readOrWrite = input("You want to read or write?:")
				
				if readOrWrite == "write":
					file1 = open("toots(1).csv",'a')
					new_message = input("Write a New toot:")
					x = file1.write(new_message)
					print(thisDict.get(i)+ x)
					myFile.close()
				
				elif readOrWrite == "read":
					with open ("toots(1).csv",'r') as file2:
						toots = csv.reader(file2)
						y = list(toots)
						print(y, end="")
						for row in toots:
							print(row[-1])
							a = handle.append(row[0])
							b = date.append(row[1])
							c = message.append(row[2])
						
					
				print(a,b,c)
				print(a,b,c)
		
		
def get_length(file_path):
		return 13
			
def append_toots(name,date,message):
		
		with open ("toots(1).csv",'a') as file2:
			toots = csv.writer(file2)
			toots.writerow({
					"handle":#print(thisDict.get(i)),
					"date":,
					"message": new_message, 
			})		
			
	append_toots("thisDict.get(i)","",new_message)	
	
'''
	
import csv	
inputFile = open("users.csv", "r")
#outputFile = open("toots(1).csv", "w")

lines = inputFile.readlines()[1:]
'''
name = []
pin = []
handle = []
following = []
total = []
toots = []
'''
for line in lines:
	print(line)
	'''
line  = line.strip()
tempList = line.split(",")
#print(len(tempList))
total.append(tempList)
name.append(tempList[1])
pin.append(tempList[2])
handle.append(tempList[0])
#following.append(tempList[3])	
	'''		
thisDict = dict(zip(pin,handle))
user = input("Enter your pin:")
		
for i in thisDict:
	if user == i:
		print(thisDict.get(i))	

class user:
	def __init__(self,handle,name,pin,following):
		self.handle = handle
		self.name = name	
		self.pin = pin
		self.following = following
		
	def read_toots(self,name,date,message):
		with open ("toots(1).csv",'r') as file2:
			toots = csv.reader(file2)
			y = list(toots)
			print(y, end="")
			for row in toots: 
				print(row[-1])
				a = handle.append(row[0])
				b = date.append(row[1])
				c = message.append(row[2])
			
			
	def append_toots(self,name,date,message):
		
		with open ("toots(1).csv",'a') as file2:
			toots = csv.writer(file2)
			toots.writerow({
					"handle:" "handle" #print(thisDict.get(i)),
					"date:" "date"
					"message:" "new_message" 
				})	

			
	if readOrWrite == "write":
		append_toots(thisDict.get(i),datetime,new_message)
	elif readOrWrite == "read":
		read_toot(thisDict.get(i),datetime,new_message)	
	else:
		print("no such option for now, sorry")	
			
			
			
			
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
			
			
			
			
			
			
			
			
			
