def get_number(prompt):
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:
            print("That is not a number. Try again.")

def main():
    print("Unbreakable divider")
    a = get_number("Enter the first number: ")
    b = get_number("Enter the second number: ")

    try:
        print("Result:", a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero")

    print("Program finished safely.")

main()