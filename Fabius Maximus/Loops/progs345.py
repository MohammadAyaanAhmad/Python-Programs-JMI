n = int(input("Enter any natural number: "))

sum_ = 0 
for i in range(1,n+1):
	sum_ += i
print(f"\nSum of all natural numbers upto {n}: {sum_}")
print("\nMultiplication table: ")
for i in range(1,11):
	print(f"{n} times {i} = {n*i}")
fact = 1
for i in range(1,n+1):
	fact*=i
print(f"\nThe factorial is: {fact}")
