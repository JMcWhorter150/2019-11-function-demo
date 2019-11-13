# 1. Write a function make_change that accepts two argument:
#   A. total_charge = amount of money owed
#   B. payment = amount of money paid
# 2. Return a 2-dimensional tuple whose values represent bills and coins
#   (singles, fives, tens, twentys, fifties, hundreds)
#   (pennies, nickles, dimes, quarters)
#  First convert dollar amount to bills
#  Second convert cents to coins
bills = [1, 5, 10, 20, 50, 100]
coins = [1, 5, 10, 25]
def convert_dollars(dollars):
    bill_count = []
    for bill in range(len(bills) - 1, -1, -1): # -1 from bill length since computer starts at 0, goes until -1 since I want to include 0, and decrements so that we start big and get to small
        count = 0
        while dollars >= bills[bill]:
            dollars -= bills[bill]
            count += 1
        bill_count.append(count)
    bill_count.reverse()
    bill_count = tuple(bill_count)
    return bill_count

def convert_coins(cents):
    coin_count = []
    for coin in range(len(coins) - 1, -1, -1): # -1 from cent length since computer starts at 0, goes until -1 since I want to include 0, and decrements so that we start big and get to small
        count = 0
        while cents >= coins[coin]:
            cents -= coins[coin]
            count += 1
        coin_count.append(count)
    coin_count.reverse()
    coin_count = tuple(coin_count)
    return coin_count

def dollar_split(total):
    dollars = round(total, 0)
    return int(dollars)

def cent_split(total):
    cents = int(round(total - int(total), 2) * 100)
    print(cents)
    return cents

def make_change(total_charge, payment):
    change = payment - total_charge
    print(change)
    dollars = dollar_split(change)
    print(dollars)
    cents = cent_split(change)
    print(cents)
    total = (convert_dollars(dollars), convert_coins(cents))
    return total

user_bill = float(input("Give me the bill total you want to split up. "))
user_paid = float(input("Give me the amount that you paid. "))
change = make_change(user_bill, user_paid)
print(change)

def find_dollars(dollars_tuple):
    sum = 0
    for i in range(len(dollars_tuple)):
        sum += dollars_tuple[i] * bills[i]
    return sum

def find_coins(coins_tuple):
    sum = 0
    for i in range(len(coins_tuple)):
        sum += coins_tuple[i] * coins[i]
    sum /= 100
    return sum

def value_of_change(dollar_coin_tuple):
    total = 0
    dollars, coins = dollar_coin_tuple
    print(dollars)
    print(coins)
    print(find_dollars(dollars))
    print(find_coins(coins))
    total += find_dollars(dollars) + find_coins(coins)
    return total

print(value_of_change(change))
