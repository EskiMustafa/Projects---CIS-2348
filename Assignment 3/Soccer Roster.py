#Mustafa Eski
#ID: 2046388
#Reference: https://replit.com/@knuckles/8171-Ch-8-Program-Soccer-team-roster-Dictionaries-Pyt

def JerseyNumber():
    Jersey = int(input("Enter new player's jersey number:"))
    while (Jersey < 0 or Jersey > 99):
        Jersey = int(input("Error! Enter new player's jersey number :"))
    return Jersey

def PlayerRating():
    rating = int(input("Enter player's rating :"))
    while (rating < 1 or rating > 9):
        rating = int(input("Error! Enter player's rating :"))
    return rating

def menu():
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()
    choice = input("Choose an option: ")
    return choice[0]



def roster(player):
    print("Roster")
    for jersey in sorted(player):
        print("Jersey number:", jersey, ",Rating:", player[jersey])

def addPlayer(player):
    Jersey = JerseyNumber()
    rating = PlayerRating()
    player[Jersey] = rating

def deletePlayer(player):
    Jersey = JerseyNumber()
    if Jersey in player:
        player.pop(Jersey)
    else:
        print("Jersey number not found.")

def updatePlayer(player):
    Jersey = JerseyNumber()
    if Jersey in player:
        rating = PlayerRating()
        player[Jersey] = rating
    else:
        print("Jersey number not found.")


def outputRatingPlayer(player):
    rating = PlayerRating()
    print("ABOVE", rating)
    for jersey in sorted(player):
        if (player[jersey] > rating):
            print("Jersey number: ", jersey, ", Rating:", player[jersey])


def getPlayerInput(player):
    x = 0
    while x < 5:
        print("Enter player", (x + 1),"'s jersey number:", end='')
        Jersey = int(input())
        while (Jersey < 0 or Jersey > 99):
            print("Error! Enter player",(x + 1),"'s jersey number :", end='')
            Jersey = int(input())
        print("Enter player", (x + 1),"'s rating :", end='')
        rating = int(input())
        while (rating < 1 or rating > 9):
            print("Error! Enter player", (x + 1),"'s rating :", end='')
            rating = int(input())
        player[Jersey] = rating
        x = x + 1



if __name__ == "__main__":
    player = {}
    getPlayerInput(player)
    roster(player)
    while True:
        choice = menu()
        if choice == 'a':
            addPlayer(player)
        elif choice == 'd':
            deletePlayer(player)
        elif choice == 'u':
            updatePlayer(player)
        elif choice == 'r':
            outputRatingPlayer(player)
        elif choice == 'o':
            roster(player)
        elif choice == 'q':
           print ("Quit")
        else:
            print("Invalid choice.")
