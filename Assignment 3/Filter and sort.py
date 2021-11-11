#Mustafa Eski
#ID: 2046388
# Filtering List (remove negative numbers)
# Reference: https://stackoverflow.com/questions/63875821/filter-and-sort-inputed-list-of-integers-for-non-negative-numbers-python
listofnumbers = input()
list = listofnumbers.split()

numberlist = ([]) #Creating an empty list to input the numbers and then filtering them
for numbers in list:
    if int(numbers) >= 0:
        numberlist.append(int(numbers))
numberlist.sort()
for x in numberlist:
    print(x, end=' ')

