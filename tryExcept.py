try:
 
    num = int(input("Enter a number: "))
    print(num)

except ValueError:
    print("wrong Input type!!")
except ZeroDivisionError as err:
    print(err)
    