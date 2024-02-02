a = int(input("enter the value: "))
operator = input("enter the op.(+,-,*,/,%): ")
b = int(input("enter the value: "))
def calculator(a,b,operator):
    total = None
    if operator == "+":
        total = a + b
    elif operator == "-":
        total = a - b
    elif operator == "*":
        total = a * b
    elif operator == "/":
        total = a / b
    else:
        total = "invalid"
    return total