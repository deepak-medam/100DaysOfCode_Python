from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)


    num_1 = float(input("What's the first number?: "))
    for op in operations:
        print(op)
    should_continue = True


    while should_continue:
        op_symbol = input("Pick an operation from the line above: ")
        num_2 = float(input("What's the next number?: "))
        op_function = operations[op_symbol]
        result = op_function(num_1, num_2)

        print(f"{num_1} {op_symbol} {num_2} = {result}")

        continue_calc = input(f"Type 'y' to continue calculating with {result}, or type 'start' to start a new calculation or 'n' to exit: ")
        if continue_calc == 'y':
            num_1 = result
        elif continue_calc == 'start':
            should_continue = False
            calculator()
        else:
            should_continue = False

calculator()