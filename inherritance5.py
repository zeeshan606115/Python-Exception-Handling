class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def eatDrink(self):
		print("Eat Biryani and drink Coca Cola")

class Employee(Person):
	def __init__(self, name, age, eno, esal):
		super().__init__(name,age)
		self.eno = eno
		self.esal = esal

	def work(self):
		print('Coding only in python')

	def empinfo(self):
		print("Employee name: ",self.name)
		print("Employee age: ",self.age)
		print("Employee Number: ",self.eno)
		print("Employee Salary: ",self.esal)

e = Employee('Zeeshan',23, 101, 45000)
e.eatDrink()
e.work()
e.empinfo()
