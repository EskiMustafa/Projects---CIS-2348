# Mustafa Eski
#PSID: 2046388

# Word frequencies
# Reference: https://stackoverflow.com/questions/64235261/how-to-find-the-frequency-of-words-in-a-list-created-from-a-csv-file
import csv
file_name = input()
with open(file_name, 'r') as file:
    words = csv.reader(file, delimiter = ',')
    dictionary = dict()
    for word in words:
        for n in word:
            if n in dictionary:
                dictionary[n] = dictionary[n] + 1
            else:
                dictionary[n] = 1
    for l in list(dictionary.keys()):
        print("{} {}".format(l, dictionary[l]))


