# Interactive Email Generator for AstraFinPay

def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()

        # Check if empty
        if not name:
            print("Input cannot be empty. Please try again.\n")
            continue

        # Check if only letters (optional but good)
        if not name.replace(" ", "").isalpha():
            print("Invalid input! Please enter only alphabets.\n")
            continue

        return name


print("=== AstraFinPay Email Generator ===\n")

# Get valid inputs
first_name = get_valid_name("Enter first name: ")
last_name = get_valid_name("Enter last name: ")

domain = "astrafinpay.com"

# Format email
email = f"{first_name.lower()}.{last_name.lower()}@{domain}"

print(f"\nGenerated Email Address: {email}")