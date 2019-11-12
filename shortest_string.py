def shortest_string(string_list):
    shortest_string = string_list[0]
    for string in string_list:
        if len(string) < len(shortest_string):
            shortest_string = string
    return shortest_string

print(shortest_string(["this is a string", "so is this", "but", "this is not"]))
