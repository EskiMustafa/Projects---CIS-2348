#Mustafa Shabbir Eski
# PSID: 2046388
# Assignment 1: Coding Problem 1: Age Calculator

print('Birthday Calculator')
print ('Current day')
month = int(input('Month: '))
day = int(input('Day: '))
year = int(input("Year: "))

print ("When is your date of birth?")
bday_month = int(input('Month: '))
bday_day = int(input('Day: '))
bday_year = int(input("Year: "))

age = year - bday_year
if bday_month<month:
    age = age
elif bday_month > month:
    age = age

elif month == bday_month:
    if bday_day<day:
        age = age

if (month == bday_month and day == bday_day):
    print('Happy Birthday')
print('You are',age, "years old.")