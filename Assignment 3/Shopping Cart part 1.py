#Mustafa Eski
#ID: 2046388
#Reference: https://stackoverflow.com/questions/52911180/create-a-list-of-a-class-as-an-attribute-of-a-second-class-in-python

class ItemToPurchase: #creating the class
    def __init__(item): #Constructor
        item.item_name = 'none'
        item.item_price = 0
        item.item_quantity = 0

    def print_item_cost(item):
        print(item.item_name +" "+str(item.item_quantity)+" @ $"+str(item.item_price)+" = $"+ str(item.item_price * item.item_quantity))

if __name__ == "__main__": #function and creating objects inside the class and calculating the total costs
    print("Item 1")
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    item1.item_name = input("Enter the item name:\n")
    item1.item_price = int(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    print("\nItem 2")
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = int(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    total = (item1.item_price*item1.item_quantity)+(item2.item_price * item2.item_quantity)
    print("\nTotal: $" + str(total))
