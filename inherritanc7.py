class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Student(Person):
	def __init__(self, name, age, roll, marks):
		super().__init__(name, age)
		self.roll = roll
		self.marks = marks

	def __str__(self):
		return 'Name = {}\nAge={}\nRoll={}\nMarks={}'.format(self.name, self.age, self.roll, self.marks)
s = Student('Zeeshan', 23, 101, 90)
print(s)