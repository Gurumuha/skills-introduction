#calculator functions
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if x ==0 or y ==0:
        return "Error: Division by Zero"
    return x/y

#printing signs/demos
print("===Simple Calculator===")
print("Choose an Operation:")
print("1. Add (+)")
print("2. subtract (-)")
print("3. multiply (*)")
print("4. divide (/)")

#loop from here (calculator should run continuously)
while True:
    try:
        op =input("Enter your operation choice (+,-,*,/): ")
    except:
        print("Enter a valid operator")
    try:
        num1 =float(input("Enter the first number: "))
        num2 =float(input("Enter the second number: "))
    except:
        print("Enter a valid number")
        continue

    if op =='+':
        result =add(num1, num2)
    elif op =='-':
        result =subtract(num1, num2)
    elif op == '*':
        result =multiply(num1, num2)
    elif op =='/':
        result = divide(num1, num2)
    else:
        result ="Invalid operator"
    print("Result:", result)

