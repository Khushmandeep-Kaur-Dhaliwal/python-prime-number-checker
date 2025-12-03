# ----------------------------------------
#    Project: Prime Numbers in a Range
#    Description:
#    This program finds and displays all
#    prime numbers between a given range.
#    MADE BY - Harmanjot singh
# ----------------------------------------

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main program
print("===== PRIME NUMBERS IN A RANGE =====")

while True:
    try:
        # Taking input from user
        start = int(input("\nEnter the starting number: "))
        end = int(input("Enter the ending number: "))

        print(f"\nPrime numbers between {start} and {end} are:")

        # Loop to check each number in the range
        for number in range(start, end + 1):
            if is_prime(number):
                print(number, end=" ")

        print("\n-------------------------------------")

        # Asking user if they want to run again
        choice = input("Do you want to check another range? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you for using the Prime Number Checker!")
            break

    except ValueError:
        print("Invalid input! Please enter numbers only.")
