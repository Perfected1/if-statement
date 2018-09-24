is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("you are male but short")
elif not(is_male) and is_tall:
    print("Not a male but Tall")
else:
    print("you are not a male")
# comparison

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else :
        return num3

first = input()
second = input()
third = input()
print(max_num(int(first), int(second), int(third)))