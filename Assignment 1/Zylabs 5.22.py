# # Mustafa Shabbir Eski
# # PSID: 2046388
# # Zylabs 5.22: Automobile service invoice

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print ()
service1 = input("Select first service:\n")
service2 = input("Select second service:\n")
print()
print("Davy's auto shop invoice")
print()
totalamount = 0
if service1 == 'Oil change':
    print('Service 1: Oil change, $35')
    totalamount = totalamount + 35
elif service1 == 'Tire rotation':
    print('Service 1: Tire rotation, $19')
    totalamount = totalamount + 19

elif service1 == 'Car wash':
    print('Service 1: Car wash, $7')
    totalamount = totalamount + 7

elif service1 == 'Car wax':
    print('Service 1: Car wax, $12')
    totalamount = totalamount + 12

elif service1 == '-':
    print('Service 1: No service')
    totalamount = totalamount + 0

if service2 == 'Oil change':
    print('Service 2: Oil change, $35')
    totalamount = totalamount + 35

elif service2 == 'Tire rotation':
    print('Service 2: Tire rotation, $19')
    totalamount = totalamount + 19

elif service2 == 'Car wash':
    print('Service 2: Car wash, $7')
    totalamount = totalamount + 7

elif service2 == 'Car wax':
    print('Service 2: Car wax, $12')
    totalamount = totalamount + 12

elif service2 == '-':
    print('Service 2: No service')
    totalamount = totalamount + 0

print()
print('Total: ${}'.format(totalamount)) #reference: https://www.w3schools.com/python/ref_string_format.asp
