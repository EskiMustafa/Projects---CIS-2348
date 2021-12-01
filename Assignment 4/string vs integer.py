# Mustafa Eski
# PSID: 2046388
# reference: stackoverflow: https://stackoverflow.com/questions/40123395/how-to-use-try-catch-to-prevent-string-input-where-an-int-is-needed
section = input().split()
name = section [0]
names = []
age = []
while name != '-1':
    try:
        ages = int(section[1])+1
    except:
        ages = 0

    names.append(name)
    age.append(ages)
    section = input().split()
    name = section[0]
for i in range(0, len(names)):
    print('{} {}'.format(names[i],age[i]))