class P:
	a = 10
	def __init__(self):
		self.b = 20

class C(P):
	def m1(self):
		print(super().a)
		print(self.b)
		print(super().b)## It is invalid because we can't call instance variable with super() method

c = C()
c.m1()