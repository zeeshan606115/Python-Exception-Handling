try:
	print("Outer try block")
	
	try:
		print("Inner try block")
		x = int(input("Enter first number: "))
		y = int(input("Enter second number: "))
		print(x/y)

	except (ZeroDivisionError) as msg:
		print("Error message: ",msg)

	finally:
		print("Inner Finally Block")
		print("Fir se Inner Finally Block")
except(ZeroDivisionError):
	print("Outer Except Block")

finally:
	print("Outer Finally Block")
	print("Fir se Outer Finally Block")

