class P:
	a = 10
	def __init__(self):
		self.b = 20

	def m1(self):
		print("parent instance class")

	@classmethod
	def m2(cls):
		print("Parent class method")

	@staticmethod
	def m3():
		print("Parent staticmethod")

class C(P):
	pass

c = C()
print(c.a)
print(c.b)
c.m1()
c.m2()
c.m3()
