# Define a function to calculate the bill total
def calculate_bill_total():
    total = 0  # Initialize the total to zero
    while True:
        user_input = input("Enter the item price or press 'q' to quit: \n")  # Prompt the user for input
        if user_input.lower() == 'q':  # If 'q' is entered, exit the loop
            break
        try:
            item_price = float(user_input)  # Convert user input to a floating-point number
            if item_price < 0:
                print("Please enter a non-negative item price.")  # Check if the item price is non-negative
            else:
                total += item_price  # Add the item price to the total
                print(f"Order total so far: {total:.2f}")  # Display the updated total with two decimal places
        except ValueError:
            print("Invalid input. Please enter a valid item price (a number) or 'q' to quit.")  # Handle invalid input
        
    return total  # Return the final bill total

# Define the main program logic
def main():
    bill_total = calculate_bill_total()  # Call the function to calculate the bill total
    print(f"Your bill total is ${bill_total:.2f}. Thanks for shopping with us.")  # Display the final bill total

if __name__ == '__main__':
    main()  # Run the main program if this script is executed directly
