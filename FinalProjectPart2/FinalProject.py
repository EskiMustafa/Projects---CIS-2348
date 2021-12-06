# Student Name: Mustafa Eski
# Student ID: 2046388

# Modules Required
import csv
import os.path
import itertools
from datetime import datetime

# Defining Global Variables
fileNameString = ["Manufacturers", "Prices", "Service Dates"]; # Used for logging to match with index of filenames array
inputFilesArray = ["ManufacturerList.csv", "PriceList.csv", "ServiceDatesList.csv"] # Predefined array for inputfiles

manufacturerListDict = []
priceListDict = []
serviceListDict = []

fullInventoryDict = []

# Our main method that will include all the functions needed to be called
def main():
    # Execute all the functions defined
    fileExists()
    readCSV()
    createFullInventory()
    queries()

# Method to check if the input files needed exists
def fileExists():
    for file in inputFilesArray:
        if os.path.exists("assets/" + file) == False:
            print("File with name " + file + " does not exist inside assets folder")
            exit()

# Method to read the csv files and add their data to their dict variables
def readCSV():
    global manufacturerListDict
    global priceListDict
    global serviceListDict
    
    fileIndex = 0
    while fileIndex < 3:
        
        with open(("assets/" + inputFilesArray[fileIndex]), mode="r") as inputFile:
            if (fileIndex == 0):
                manufacturerListDict = list(csv.DictReader(inputFile, fieldnames=["itemId", "manufacturerName", "itemType", "itemCondition"]))
            elif (fileIndex == 1):
                priceListDict = list(csv.DictReader(inputFile, fieldnames=["itemId", "itemPrice"]))
            elif (fileIndex == 2):
                serviceListDict = list(csv.DictReader(inputFile, fieldnames=["itemId", "serviceDate"]))
            
        fileIndex += 1

# Output require a - Created a list of all items listed by row with all their information
def createFullInventory():
    global fullInventoryDict
    itemPrice = ""
    serviceDate = ""

    fullInventoryDict = sorted(manufacturerListDict, key=lambda d: d["manufacturerName"]) 
    
    for inventoryRow in fullInventoryDict:
        for priceRows in priceListDict:
            if (priceRows["itemId"] == inventoryRow["itemId"]):
                itemPrice = priceRows["itemPrice"]
                break
        for serviceRows in serviceListDict:
            if (serviceRows["itemId"] == inventoryRow["itemId"]):
                serviceDate = serviceRows["serviceDate"]
                break
        inventoryRow.update({"itemPrice": itemPrice, "serviceDate": serviceDate})

# Ask users for their query and perform the search
def queries():
    print("Eski Electronics Store\n")
    userInput= input("Please enter the product name you are looking for: ")

    if userInput.lower() == "q" or userInput.lower() == "quit":
        exit()
    
    manufractureIndexes = []
    productTypeIndexes = []

    newInventoryList = filterInventory()

    # checks all the products and each word and checking if the manufacturer name and itemtype is available and add their index within the list to their according list
    rowIndex = 0
    for row in newInventoryList:
        for word in userInput.split():
            if word.lower().replace(" ", "") == row["manufacturerName"].lower().replace(" ", ""):
                manufractureIndexes.append(rowIndex)
            if word.lower().replace(" ", "") == row["itemType"].lower().replace(" ", ""):
                productTypeIndexes.append(rowIndex)
        rowIndex += 1

    matchingIndexes = []

    # checks if manufracture and products list have matching indexes and created a new array of indexes with both matching criteria 
    for manuIdx in manufractureIndexes:
        for typeIdx in productTypeIndexes:
            if manuIdx == typeIdx:
                matchingIndexes.append(typeIdx)
                break

    # Print if there are any matching product type + manufracture that user searched for else give out an error
    if len(matchingIndexes) > 0:
        print("We have found " + str(len(matchingIndexes)) + " search results:")

        for index in matchingIndexes:
            print("- " + newInventoryList[index]["itemId"] + " | " + newInventoryList[index]["manufacturerName"].replace(" ", "") + " " + newInventoryList[index]["itemType"] + " | $" + newInventoryList[index]["itemPrice"])
    else:
        print("We have not found any results related to your search. Such item may not exist in our inventory.")

    newManList = manufractureIndexes
    newProdList = productTypeIndexes

    # Creates a new indexes list to remove index if they are already displayed in matching results
    for idx in matchingIndexes:
        for manuIdx in newManList:
            if manuIdx == idx:
                newManList.remove(idx)
        for typeIdx in newProdList:
            if typeIdx == idx:
                newProdList.remove(idx)

    # Prints out list of products of type searched from other manufracturers or other products from same manufracturer
    if len(newProdList) > 0:
        if len(newManList) == 0:
            print("\nYou may also consider these products from other manufractures: ")
            for index in newProdList:
                print("- " + newInventoryList[index]["itemId"] + " | " + newInventoryList[index]["manufacturerName"].replace(" ", "") + " " + newInventoryList[index]["itemType"] + " | $" + newInventoryList[index]["itemPrice"])    
    elif len(newManList) > 0:
        print("\nYou may also consider these other products from the same manufracture: ")
        for index in newManList:
            print("- " + newInventoryList[index]["itemId"] + " | " + newInventoryList[index]["manufacturerName"].replace(" ", "") + " " + newInventoryList[index]["itemType"] + " | $" + newInventoryList[index]["itemPrice"])

    print("\nType q or Q to quit\n")
    queries()
        
# creates a new list of inventory to remove damaged or products past their service date
def filterInventory():
    indexes = []

    # Checks each item in inventory if its damaged or past serviced date and notes their index
    idx = 0
    for rows in fullInventoryDict:
        changed = False
        if datetime.strptime(rows["serviceDate"].replace("/", "-"), "%m-%d-%Y") < datetime.today():
            indexes.append(idx)
            changed = True
        if rows["itemCondition"] == "damaged" and changed == False:
            indexes.append(idx)
        idx += 1

    newList = fullInventoryDict

    # Creates a new list and remove all the filtered items not needed to be displayed
    idx = 0
    for delIdx in indexes:
        del newList[delIdx - idx]
        idx += 1

    return newList

# Run the main() once all the functions are definied
main()
