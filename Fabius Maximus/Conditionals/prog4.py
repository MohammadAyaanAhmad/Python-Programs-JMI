num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2:
	if num3 > num1:
		print(f"{num3} is greatest.")
	else:
		print(f"{num1} is greatest.")
else:
	if num2 > num3:
		print(f"{num2} is greatest.")
	else:
		print(f"{num3} is greatest.")
