def longest_string(string_list):
    longest_string = string_list[0]
    for string in string_list:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

print(longest_string(["this is a string", "so is this", "but", "this is not"]))