def largest_number(number_list):
    largest = number_list[0]
    for number in number_list:
        if number >= largest:
            largest = number
    return largest

print(largest_number([1, 3, 1900, 7, 19, -1]))