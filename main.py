import re

def check_password_strength(password):
    strength = 0

    # Length check
    if len(password) >= 8:
        strength += 1

    # Presence of uppercase and lowercase letters
    if re.search("[A-Z]", password) and re.search("[a-z]", password):
        strength += 1

    # Presence of digits
    if re.search("[0-9]", password):
        strength += 1

    # Presence of special characters
    if re.search("[!@#$%^&*()-_=+{};:,<.>]", password):
        strength += 1

    return strength

def assess_strength(strength):
    if strength == 0:
        return "Very Weak"
    elif strength == 1:
        return "Weak"
    elif strength == 2:
        return "Moderate"
    elif strength == 3:
        return "Strong"
    elif strength == 4:
        return "Very Strong"

# Example usage
password = input("Enter a password: ")
strength = check_password_strength(password)
strength_description = assess_strength(strength)
print("Password strength:", strength_description)
