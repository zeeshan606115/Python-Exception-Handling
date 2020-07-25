try:
	x = int(input("Enter first number: "))
	y = int(input("Enter second number: "))
	print(x/y)
except (ZeroDivisionError, ValueError) as msg:
	print("Error message: ",msg)
