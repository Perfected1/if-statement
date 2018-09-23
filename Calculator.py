
num1 = float(input("Enter a number:  "))

op = input("Enter a operator:  ")

num2 = float(input("Enter a number:  "))
if op == "+":
    print(int(num1) + int(num2))
elif op == "-":
    print(int(num1) - int(num2))
elif op == "/":
    print(int(num1) / int(num2))
elif op == "*":
    print(int(num1) * int(num2))
else:
    print("INVALID OPERATOR!!!")