import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected.")

    return ''.join(random.choice(characters) for _ in range(length))

def get_boolean_input(prompt):
    while True:
        choice = input(prompt + " (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Please enter 'y' or 'n'.")

def main():
    print("\n🔐 Welcome to SecurePass Generator!\n")

    while True:
        try:
            length = int(input("Enter password length (min 4): "))
            if length < 4:
                print("⚠️ Password length must be at least 4.\n")
                continue

            use_uppercase = get_boolean_input("Include uppercase letters?")
            use_numbers = get_boolean_input("Include numbers?")
            use_symbols = get_boolean_input("Include symbols?")

            password = generate_password(length, use_uppercase, use_numbers, use_symbols)
            print(f"\n✅ Your secure password is:\n👉 {password}\n")

            again = get_boolean_input("Generate another password?")
            if not again:
                print("\nThank you for using SecurePass Generator! 🔒")
                break
        except ValueError as ve:
            print(f"Error: {ve}\n")
