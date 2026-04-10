string = input("Enter a string: ")

#1. Find lenght
length = len(string)

#2. Reverse a string
reversedString = ""

for i in range(length-1,-1,-1):
    reversedString += string[i]

print(reversedString)

#3. Check pallindrome

if string == reversedString:
    print("Palindrome detected.")
else:
    print("Not a pallindrome.")

#4. Count the number of vowels

vowelCount = 0

for i in string:
    if i in "aeiouAEIOU":
        vowelCount += 1

print(vowelCount)

#5. Convert to uppercase and lowercase

print("Upper case:", string.upper())
print("Lower case:", string.lower())

