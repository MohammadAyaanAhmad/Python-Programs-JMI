#1
my_list = [4,7,6,7,1,3,9,6,11,0,1,4,4,6,0,7]
print(my_list)

#2
sum_ = 0
for i in my_list:
    sum_ += i
print(f"\n{sum_} is the sum of the elements in the list.\n")


#3
print(f"The largest element is {max(my_list)} and the smallest is {min(my_list)}.\n")

#4
occ = {}

#initializing
for i in my_list:
    occ[i] = 0

#counting
for j in my_list:
    occ[j]+=1

#printing
for h in occ:
    print(f"{h} occurred {occ[h]} times")

#5

my_list.reverse()
print("\nThe reversed list is: ")
print(my_list)
