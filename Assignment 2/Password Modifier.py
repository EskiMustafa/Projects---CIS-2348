#Mustafa Shabbir Eski
# PSID: 2046388
# Assignment 6.17 CIS 2348 LAB: Password modifier

password = input()
answer = ""
p = 0
while p < len(password):
    letters = password[p]
    if letters == 'i':
        answer = answer + '!'
    elif letters == 'a':
        answer = answer + '@'
    elif letters == 'm':
        answer = answer + 'M'
    elif letters == 'B':
        answer = answer + '8'
    elif letters == 'o':
        answer  = answer + '.'
    else:
        answer=answer+letters
    p +=1
answer+='q*s'
print (answer)