# Mustafa Shabbir Eski
# PSID: 2046388
# Palindrome
# Reference = https://www.geeksforgeeks.org/sentence-palindrome-palindrome-removing-spaces-dots-etc/

palindrome =  input()
l = 0
h = len(palindrome)-1
result = True
while(l<h):
    if(palindrome[l]==' '):
        l = l + 1
    elif(palindrome[h]==' '):
        h = h - 1
    elif(palindrome[l]!= palindrome[h]):
        result = False
        break
    else:
        l+= 1
        h -= 1
if (result):
    print(palindrome, "is a palindrome")
else:
    print(palindrome, "is not a palindrome")

