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
    
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Welcome to SecurePass Generator!")
    try:
        length = int(input("Enter the desired password length (min 4): "))
        if length < 4:
            print("Password length must be at least 4.")
            return
        
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        print(f"Your generated password is: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
