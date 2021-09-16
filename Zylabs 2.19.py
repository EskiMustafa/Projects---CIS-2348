# Mustafa Shabbir Eski
# PSID: 2046388
# Zylabs 2.19: Program cooking Measurement converter

lemonjuice = float(input("Enter amount of lemon juice (in cups):\n"))
water = float(input("Enter amount of water (in cups):\n"))
agave = float(input("Enter amount of agave nectar (in cups):\n"))
servings = float(input('How many servings does this make?\n'))
print()
print ('Lemonade ingredients - yields','{:.2f}'.format(servings),'servings')
print ('{:.2f}'.format(lemonjuice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave), 'cup(s) agave nectar\n')

serv = float(input("How many servings would you like to make?\n"))
lemonjuice = ((lemonjuice/6)*serv)
water = ((water/6)*serv)
agave = ((agave/6)*serv)
print()
print('Lemonade ingredients - yields', '{:.2f}'.format(serv), 'servings')
print('{:.2f}'.format(lemonjuice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(agave), 'cup(s) agave nectar')
print()
print('Lemonade ingredients - yields','{:.2f}'.format( serv), 'servings')
lemonjuice = lemonjuice/16
water = water/16
agave = agave/16
print ('{:.2f}'.format(lemonjuice), 'gallon(s) lemon juice')
print('{:.2f}'.format(water),'gallon(s) water')
print('{:.2f}'.format(agave), 'gallon(s) agave nectar')