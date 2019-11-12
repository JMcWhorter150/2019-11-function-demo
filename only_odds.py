def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_odd(number):
    if is_even(number) != True:
        return True
    else:
        return False

def only_odds(number_list):
    new_list = []
    for number in number_list:
        if is_odd(number) == True:
            new_list.append(number)
    return new_list

print(only_odds([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))