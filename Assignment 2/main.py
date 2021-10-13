def exact_change(user_total):
    dollars = user_total // 100
    user_total = user_total % 100
    quarters = user_total // 25
    user_total = user_total % 25
    dimes = user_total // 10
    user_total = user_total % 10
    nickels = user_total // 5
    user_total = user_total % 5
    pennies = user_total
    return (dollars, quarters, dimes, nickels, pennies)
if __name__ == '__main__':
    input_val = int(input())
    dollars, quarters, dimes, nickels, pennies = exact_change(input_val)

    if input_val <= 0:
        print ('no change')
    else:
        if dollars > 1:
            print('%d dollars' % dollars)
        elif dollars == 1:
            print('%d dollar' % dollars)
        if quarters > 1:
            print('%d quarters' % quarters)
        elif quarters == 1:
            print('%d quarter' % quarters)
        if dimes > 1:
            print('%d dimes' % dimes)
        elif dimes == 1:
            print('%d dime' % dimes)
        if nickels > 1:
            print('%d nickels' % nickels)
        elif nickels == 1:
            print('%d nickel' % nickels)
        if pennies > 1:
            print('%d pennies' % pennies)
        elif pennies == 1:
            print('%d penny' % pennies)
