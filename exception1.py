try:
	x = int(input("Enter first number: "))
	y = int(input("Enter second number: "))
	print(x/y)
except ZeroDivisionError as msg:
	print("Error message: ",msg)
except ValueError as msg:
	print("Provide int value only: ",msg)