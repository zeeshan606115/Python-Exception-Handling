class P:
	a = 10
	def __init__(self):
		self.b = 20

	def m1(self):
		print("Parent Instance Method!!")

	@classmethod
	def m2(cls):
		print("Parent class Method!!")

	@staticmethod
	def m3():
		print("Parent Static Method!!")

class C(P):
	a  = 999
	def __init__(self):
		self.b = 1000
		super().__init__()
		print(super().a)
		super().m1()
		super().m2()
		super().m3()
		print(C.a)
c = C()