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
print(is_odd(3))
print(is_odd(4))