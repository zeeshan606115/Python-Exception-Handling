try:
	x = int(input("Enter first number: "))
	y = int(input("Enter second number: "))
	print(x/y)

except (ZeroDivisionError) as msg:
	print("ZeroDivisionError: can't divide zero: ",msg)
except:
	print("Default Exception: provide valid value")

