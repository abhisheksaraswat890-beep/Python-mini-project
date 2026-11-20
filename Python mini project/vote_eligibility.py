
# Vote Eligibility Checker
# Python Based Mini Project

def check_eligibility():
    print("\n================================")
    print("     VOTE ELIGIBILITY CHECKER")
    print("================================")

    name = input("Enter your name: ")

    try:
        age = int(input("Enter your age: "))

        if age < 0:
            print("Invalid age! Please enter a valid age.")

        elif age >= 18:
            print("\nCongratulations", name, "!")
            print("You are ELIGIBLE to vote.")
            print("Minimum voting age requirement is fulfilled.")

        else:
            print("\nSorry", name, "!")
            print("You are NOT ELIGIBLE to vote.")
            print("You must be at least 18 years old.")

    except ValueError:
        print("Invalid input! Please enter age in numbers.")


# Main Program
while True:
    check_eligibility()

    choice = input("\nDo you want to check again? (yes/no): ")

    if choice.lower() != "yes":
        print("\nThank you for using Vote Eligibility Checker!")
        break
