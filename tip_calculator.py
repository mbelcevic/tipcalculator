def get_number(prompt, number_type=float):
    while True:
        user_input = input(prompt)
        try:
            # Try converting the input to the specified type (float or int)
            number = number_type(user_input)
            return number
        except ValueError:
            # If conversion fails, print an error message and ask again
            print("Please enter a valid number.")

def get_positive_float(prompt):
    while True:
        value = get_number(prompt, float)
        if value >= 0:
            return value
        print("Please enter a non-negative number.")

def get_positive_int(prompt):
    while True:
        value = get_number(prompt, int)
        if value > 0:
            return value
        print("Please enter a number greater than 0.")

print("Welcome to the tip calculator!")

bill_amount = get_positive_float("How much was the bill? ")
print("Thank you.")       

tip_percent = get_positive_float("How much tip would you like to give? Please enter a % number: ")
print("Thank you.")
            
people_number = get_positive_int("How many people would split the bill? ")
print("Thank you.")

# Calculate the tip per person
tip_per_person = (bill_amount * (1 + (tip_percent / 100))) / people_number

# Format the tip to two decimal places
print(f"Each person should pay: ${tip_per_person:.2f}")
