class Parent():
	def __init__(self,last_name,eye_color):
		print ("Parent constructor called")
		self.last_name = last_name
		self.eye_color = eye_color

class Child(Parent):
	def __init__(self, last_name, eye_color, number):
		print ('Child constructor')
		Parent.__init__(self, last_name, eye_color)
		self.number = number

#billy_cyrus = Parent('Cyrus','blue')
#print (billy_cyrus.last_name)

miley_cyrus = Child('Cyrus', 'blue' , '5')
print (miley_cyrus.last_name)
print (miley_cyrus.number)