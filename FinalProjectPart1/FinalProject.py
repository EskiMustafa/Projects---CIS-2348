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
    # If users would like to use files with custom names we will change our global variables
    changeDefaultFiles = input("Would you like to change default filenames?\nType Y for yes and N for No: ")
    
    if changeDefaultFiles.lower() != "y" and changeDefaultFiles.lower() != "n":
        main()
    elif changeDefaultFiles.lower() == "y":
        changeInputFiles()

    # Execute all the functions defined
    fileExists()
    readCSV()
    createFullInventory()
    categorizeByType()
    pastServiceData()
    damagedItems()

# Method to change the file names if needed by user
def changeInputFiles():
    iFAIDX = 0
    while iFAIDX < 3:
        inputFilesArray[iFAIDX] = input("Please enter the " + fileNameString[iFAIDX] + " List CSV file name with filetype (.csv): ")
        iFAIDX += 1

# Method to check if the input files needed exists
def fileExists():
    for file in inputFilesArray:
        if os.path.exists("assets/" + file) == False:
            print("File with name " + file + " does not exist inside assets folder")
            changeInputFiles()

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

# Write CSV when called by a function - accepts file name and list of rows
def writeCSV(filename, dictlist, fieldnames):
    with open("output/" + filename + ".csv", "w", newline="") as outputFile:
        writer = csv.DictWriter(outputFile, fieldnames=fieldnames)
        for row in dictlist:
            writer.writerow(row)

# Order Dictionary in specific key orders
def orderDict(dictList, orderList):
    idx = 0
    while idx < len(dictList):
        newDict = dict()
        for key in orderList:
            newDict[key] = dictList[idx][key]
        dictList[idx] = newDict
        idx += 1

    return dictList

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

    sortFullInventory = ["itemId", "manufacturerName", "itemType", "itemPrice", "serviceDate", "itemCondition"]
    fullInventoryDict = orderDict(fullInventoryDict, sortFullInventory)

    writeCSV("FullInventory", fullInventoryDict, fullInventoryDict[0].keys())

# Categorize list by types available within the file
def categorizeByType():
    newList = sorted(fullInventoryDict, key=lambda d: d["itemType"]) 
    
    idx = 0
    valAddLast = 0
    lastValNext = False
    previousChangeIndex = 0
    previousType = newList[0]["itemType"]

    for row in newList:
        if idx + 1 == len(newList):
                lastValNext = True
                valAddLast = 1
        if row["itemType"] != previousType or lastValNext == True:
            tempList = sorted(newList[previousChangeIndex:idx + valAddLast], key=lambda d: d["itemId"]) 
            writeCSV(previousType + "Inventory", tempList, newList[idx].keys())
            previousType = row["itemType"]
            previousChangeIndex = idx
        idx += 1
        
# Checks if an item has service date before today and creates a list
def pastServiceData():
    newList = []
    
    for rows in fullInventoryDict:
        if datetime.strptime(rows["serviceDate"].replace("/", "-"), "%m-%d-%Y") < datetime.today():
            newList.append(rows)
            
    newList = sorted(newList, key=lambda d: d["serviceDate"], reverse=True)
    
    writeCSV("PastServiceDateInventory", newList, newList[0].keys())

# List of items that has damaged condition
def damagedItems():
    newList = []

    for rows in fullInventoryDict:
        if rows["itemCondition"] == "damaged":
            newList.append(rows)

    for row in newList:
        del row["itemCondition"]

    writeCSV("DamagedInventory", newList, newList[0].keys())

# Run the main() once all the functions are definied
main()
