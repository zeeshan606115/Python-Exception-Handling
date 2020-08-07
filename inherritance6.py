class Car:
	def __init__(self, name, model, color):
		self.name = name
		self.model = model
		self.color = color

	def getInfo(self):
		print("\tCar Name: {}\n\tModel: {}\n\tColor: {}".format(self.name, self.model, self.color))

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def eatDrink(self):
		print("Eat Biryani and drink Coke")

class Employee(Person):
	def __init__(self, name, age, eno, esal, car):
		super().__init__(name, age)
		self.eno = eno
		self.esal = esal
		self.car = car

	def work(self):
		print("Coding Python only!!")

	def empInfo(self):
		print("Employee Name: ",self.name)
		print("Employee Age: ",self.age)
		print("Employee Car: ")
		self.car.getInfo()

		print("Employee Number: ",self.eno)
		print("Employee Salary: ",self.esal)
		
c = Car('Innova', '2.5V', "Grey")
e = Employee('Zeeshan',24, 1001, 100000, c)
e.eatDrink()
e.work()
e.empInfo()