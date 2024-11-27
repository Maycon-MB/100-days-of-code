from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }

def calculator():
    print(logo)
    should_acummulate = True
    num1 = float(input("What's the first number? \n"))

    while should_acummulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operator: \n")            
        num2 = float(input("What's the second number? \n"))

        answer = operations[operation_symbol](num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_acummulate = False
            print("\n" * 20)
            calculator()

calculator()            






