def only_evens(number_list):
    new_list = []
    for number in number_list:
        if number % 2 == 0:
            new_list.append(number)
    return new_list
print(only_evens([2, 3, 4, 5, 6, 7, 8, 10]))