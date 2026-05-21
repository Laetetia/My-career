def run_calculator():
    print("--- Simple Terminal Calculator ---")
    while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
        return

    
    operator = input("Enter an operator (+, -, *, /): ").strip()

    
    if operator == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operator == '/':
        
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Invalid operator. Please use +, -, *, or /.")
        continue
    choice = input("\nDo you want to perform another calculation? (y/n): ").strip().lower()
        if choice != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    run_calculator()