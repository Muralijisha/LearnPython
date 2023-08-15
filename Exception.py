try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print("Invalid age")
except ZeroDivisionError:
    print("Age should not be Zero")