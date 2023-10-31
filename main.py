sum = 0

while True:
    userInput = input("Enter the item price or press 'q' to quit: \n")
    if userInput.lower() == 'q':
        break
    try:
        item_price = float(userInput)
        if item_price < 0:
            print("Please enter a non-negative item price.")
        else:
            sum += item_price
            print(f"Order total so far: {sum}")
    except ValueError:
        print("Invalid input. Please enter a valid item price (a number) or 'q' to quit.")

print(f"Your Bill total is ${sum:.2f}. Thanks for shopping with us.")
