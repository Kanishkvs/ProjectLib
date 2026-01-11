import string
import random
def generate_passw1ord(length=13):
    if length < 12:
        print("Password length should be at least 12 characters.")
        return None
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = lower + upper + digits + symbols

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return "".join(password)
def check_password(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    long_enough = len(password) >= 8
    if not long_enough:
        print(" Password must be at least 8 characters long.")
    if not has_lower:
        print(" Must contain at least one lowercase letter.")
    if not has_upper:
        print(" Must contain at least one uppercase letter.")
    if not has_digit:
        print(" Must contain at least one digit.")
    if not has_symbol:
        print(" Must contain at least one special character (!@#$ etc).")
    if all([has_lower, has_upper, has_digit, has_symbol, long_enough]):
        return True
    else:
        return False
def verify_password(entered_password, correct_password):

    if entered_password == correct_password:
        return True
    else:
        return False
def main():
    choice = input("Do you want to (1) Generate a strong password or (2) Enter your own password? (Enter 1 or 2): ")

    if choice == '1':
        password_length = int(input("Enter desired password length (minimum 8 characters): "))
        generated_password = generate_password(password_length)
        print(f"Generated password: {generated_password}")
        if generated_password and check_password(generated_password):
            print(f"Password '{generated_password}' is strong enough!")
            password_to_check = input("Enter the password to verify: ")
            if verify_password(password_to_check, generated_password):
                print("Password is correct!")
            else:
                print("Password is incorrect.")
        else:
            print("The password is not strong enough.")

    elif choice == '2':
        user_password = input("Enter your password: ")
        if check_password(user_password):
            print(f"Password '{user_password}' is strong enough!")
            password_to_check = input("Enter the password to verify: ")
            if verify_password(password_to_check, user_password):
                print("Password is correct!")
            else:
                print("Password is incorrect.")
        else:
            print("The password is not strong enough.")

    else:
        print("Invalid choice. Please enter 1 or 2.")
        
main()
