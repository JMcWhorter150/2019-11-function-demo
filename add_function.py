def add(num1, num2):
    sum = num1 + num2
    return sum

print(add(1, 1))

print(add(add(1,1), 1))

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print(divide(multiply(subtract(add(add(2, 4), 1), 2), 10), 5))