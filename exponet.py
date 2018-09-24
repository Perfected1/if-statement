def exponent(num, multiply):
    result = 1
    for index in range(multiply):
        result = result * num
    return result

num = input("Enter Number: ")
multiply = input("Raise to Power of: ")

print(exponent(int(num), int(multiply)))