y = int(input("Enter a year: "))
yes = "Leap year"
no = "Not a leap year"


if y%4:
	print(no)
else:
	if y%100:
		print(yes)
	else:
		if y%400:
			print(no)
		else:
			print(yes)
