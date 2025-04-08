def calculate(x, y, oper):
    if oper == "+":
        return x + y
    elif oper == "-":
        return x - y
    elif oper == "*":
        return x * y
    elif oper == "/":
        return x / y


answer = int(input("Enter the first number >> "))
finished = False
while not finished:
    operation = input("Enter the next operation (+, -, *, /) or '=' to finish or 'c' to restart >> ")
    if operation in ["+", "-", "*", "/"]:
        number = int(input("Enter the next number >> "))
        answer = calculate(answer, number, operation)
    elif operation == "=":
        print("Finishing...")
        print("The answer is", answer)
        finished = True
    elif operation == "c":
        print("Restarting...")
        answer = 0
    else:
        print("Invalid operation!")
