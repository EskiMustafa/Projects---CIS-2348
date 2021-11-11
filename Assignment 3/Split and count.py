#Mustafa Eski
# ID: 2046388
#reference: https://stackoverflow.com/questions/22101086/split-and-count-a-python-string

words = input()
wordsplit = words.split(" ")

for term in wordsplit:
    print(term, wordsplit.count(term))
