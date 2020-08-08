class P:
	def __init__(self):
		print("Parent Method!!")

class C(P):
	def m2(self):
		print("Child Method!!!")

c = C()
c.m2()

