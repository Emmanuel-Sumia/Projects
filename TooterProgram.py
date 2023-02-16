'''
TOOTER PROGRAM By Emmanuel John Sumia
'''



from datetime import datetime #googled how to import datetime
import csv
from csv import writer

today = datetime.today().strftime("%m/%d/%Y")

inputFile = open("users.csv", "r")

csv_reader = csv.DictReader(inputFile)

  # csv dictreader method which reads the entire users.csv in a comma separated format
  
print("WELCOME TO TOOTER..") #program initialization

#A class for our program

class All:
	
	# Below are the Functions which help us to perform the task
	
	def __init__(self,handles=[],pins=[],index=[],names=[],following=[]):
		self.handles = handles
		self.pins = pins
		self.index = index
		self.names = names
		self.following = following
		
	def readCsv(self):
		for lines in csv_reader:
			
		#i appended the empty lists i created with the corresponding values in the users.csv file
			self.handles.append(lines["handle"])
			self.pins.append(lines["pin"])           
			self.names.append(lines["name"])
			self.following.append(lines["following"])

	
	def checkForPins(self): #first function which asks for the right pin so as to identify the user.
		
		self.readCsv()
		user = input("Please insert pin:")
		
		if user not in self.pins:
			print("Wrong pin, please retry")
			self.checkForPins() # if the user inputs a wrong pin this recursive call prompts him to retry
			
		else:
			number_index = self.pins.index(user)
			self.index.append(number_index)
		
			print("Hello", self.handles[number_index],":)") #welcomes the identified user
			

		
		
		
# Second function which prompts the user to select his choice of either writing or reading.
	
	def readorwrite(self):
		
		readwrite = (input("Do you want to read toots or write a new toot? ")).lower()
		self.readCsv()
		
		#conditional statements based on the user's choice and typing mistake
	
		if readwrite == "read":
	
			def read_toots():
			
				if self.following[self.index[0]] == None:
					print("No toots Available")
				else:
					i = self.following[self.index[0]].split("-") #we split the 
				
					file1 = open("toots.csv",'r')
					csv_reader2 = csv.reader(file1)
       
					for line in csv_reader2:
						
						if line[0] in i:
							print("On " + line[1] + " " + line[0] + " tooted: " + line[2])
						
					file1.close()
		
			read_toots()
			
		elif readwrite == "write":
	
			def append_toots():	
							
				new_message = input("Write a new toot:")
			
				new_toot = [self.handles[self.index[0]],today,new_message]
	
				file2 = open("toots.csv", "a")
			
				csv_writer = writer(file2)
				csv_writer.writerow(new_toot)
	
				file2.close()
				
			append_toots()
			
		elif readwrite != "read" or readwrite != "write":
			self.readorwrite() # if the user fo any reason doesn't input the correct write or read options or even an empty string it prompts him to reselect option
		
				
# main function of the program
def main():
	c = All()
	c.checkForPins()	
	c.readorwrite()

	
if __name__== "__main__":
	main()

	













		
	
		
