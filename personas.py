
class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def say_hello(self):
		print('Hello. My name is {} and  i am {} years old'.format(self.name,self.age))



if __name__ == '__main__':
	person =  Person('JACD','21')

	print('Age: {}'.format(person.age))
	person.say_hello() 