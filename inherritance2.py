class Car:
	def __init__(self, name, model, color):
		self.name = name
		self.model = model
		self.color = color

	def getInfo(self):
		print("Car Name:{}, model: {}, and color: {}".format(self.name, self.model, self.color))


class Employee:
	def __init__(self, ename, eno, car):
		self.ename = ename 
		self.eno = eno
		self.car = car

	def empInfo(self):
		print("Employee name: ",self.ename)
		print("Employee number: ",self.eno)
		print("Employee car Info: ")
		self.car.getInfo()

c = Car('XUV',500, "Black")
e = Employee('Zeeshan',101,c)
e.empInfo()