def smallest_number(number_list):
    smallest = number_list[0]
    for number in number_list:
        if number <= smallest:
            smallest = number
    return smallest

print(smallest_number([1, 3, 4, 7, -1, 19, 21]))