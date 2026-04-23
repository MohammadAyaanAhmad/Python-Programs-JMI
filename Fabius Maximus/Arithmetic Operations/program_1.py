#Perform addition, subtraction, multiplication and division

a = int(input('Enter a number: '))
b = int(input('Enter another number: '))

print("Sum:", a+b)
print("Difference:", a-b)
print("Product:", a*b)
if b != 0:
	print("Quotient:",a/b)
else:
	print("Cannot divide by zero.")
