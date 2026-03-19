# Interactive OSINT Risk Scoring System

def get_valid_input(question):
    while True:
        answer = input(question).strip().lower()

        if answer in ["yes", "no"]:
            return answer
        else:
            print("Invalid input! Please enter 'yes' or 'no'.\n")


print("=== OSINT Risk Assessment Tool ===\n")

score = 0

# Email Exposure
email = get_valid_input("Is email pattern predictable? (yes/no): ")
if email == "yes":
    score += 3

# Subdomain Exposure
subdomain = get_valid_input("Are subdomains exposed? (yes/no): ")
if subdomain == "yes":
    score += 2

# Employee Data Exposure
employee = get_valid_input("Is employee information publicly available? (yes/no): ")
if employee == "yes":
    score += 5

# Final Result
print("\n--- Final Risk Assessment ---")
print(f"Total Risk Score: {score}/10")

if score >= 7:
    print("Risk Level: HIGH")
elif score >= 4:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: LOW")