import string

def analyze_password(password):
    score = 0
    length = len(password)

    # Check length
    if length >= 8:
        score += 1
    else:
        print("❌ Too short (minimum 8 characters)")

    # Check uppercase
    if any(char.isupper() for char in password):
        score += 1
    else:
        print("❌ Add at least one uppercase letter")

    # Check lowercase
    if any(char.islower() for char in password):
        score += 1
    else:
        print("❌ Add at least one lowercase letter")

    # Check digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        print("❌ Add at least one digit")

    # Check special characters
    special_chars = string.punctuation
    if any(char in special_chars for char in password):
        score += 1
    else:
        print("❌ Add at least one special character (e.g., @, #, $)")

    # Determine strength
    print("\nPassword Strength:")
    if score == 5:
        print("✅ Strong 💪")
    elif score >= 3:
        print("⚠️ Moderate 😐")
    else:
        print("❌ Weak 😟")

# Main program
if __name__ == "__main__":
    pwd = input("Enter your password to analyze: ")
    print("\nAnalyzing...")
    analyze_password(pwd)
