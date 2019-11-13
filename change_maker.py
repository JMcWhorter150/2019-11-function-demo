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
    # print(dollars)
    bill_count = []
    for bill in range(len(bills) - 1, -1, -1): # -1 from bill length since computer starts at 0, goes until -1 since I want to include 0, and decrements so that we start big and get to small
        # print(bills[bill])
        count = 0
        while dollars >= bills[bill]:
            dollars -= bills[bill]
            count += 1
        bill_count.append(count)
    # print(bill_count)
    bill_count.reverse()
    bill_count = tuple(bill_count)
    # print(bill_count)
    return bill_count

def convert_coins(cents):
    # print(cents)
    coin_count = []
    for coin in range(len(coins) - 1, -1, -1): # -1 from cent length since computer starts at 0, goes until -1 since I want to include 0, and decrements so that we start big and get to small
        # print(coins[coin])
        count = 0
        while cents >= coins[coin]:
            cents -= coins[coin]
            count += 1
        coin_count.append(count)
    # print(coin_count)
    coin_count.reverse()
    coin_count = tuple(coin_count)
    # print(coin_count)
    return coin_count

def dollar_split(total):
    dollars = round(total, 0)
    return int(dollars)

def cent_split(total):
    cents = int((total - dollar_split(total)) * 100)
    return cents

def make_change(total_charge, payment):
    change = payment - total_charge
    dollars = dollar_split(change)
    cents = cent_split(change)
    total = (convert_dollars(dollars), convert_coins(cents))
    return total


# convert_coins(175)
# convert_dollars(150)

# print(dollar_split(173.31))
# print(cent_split(173.31))

user_bill = float(input("Give me the bill total you want to split up. "))
user_paid = float(input("Give me the amount that you paid. "))
print(make_change(user_bill, user_paid))













#     reverse_bills = []
#     # reverse_bills.reverse()
#     # print(reverse_bills)
#     for bill in range(len(bills), 0, -1):
#         count = 0
#         print(bills[bill])
#         while dollars > bills[bill]:
#             count += 1
#             dollars -= bills[bill]
#             print(count)
#         reverse_bills.append(count)
#     # reverse_bills = reverse_bills.reverse()
#     # total_bills = tuple(reverse_bills)
#     # return total_bills
#     return reverse_bills
# print(convert_dollars(400))
    
    

