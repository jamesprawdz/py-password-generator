import random
import string

# Function to generate a random password with the specified criteria
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Create a character set based on the user's preferences
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    # Initialize an empty list to store the password characters
    pwd = []

    # Ensure at least one number is included if the user requests numbers
    if numbers:
        pwd.append(random.choice(digits))

    # Ensure at least one special character is included if the user requests special characters
    if special_characters:
        pwd.append(random.choice(special))

    # Add random characters until the desired password length is reached
    while len(pwd) < min_length:
        pwd.append(random.choice(characters))

    # Shuffle the characters to create a randomized password
    random.shuffle(pwd)

    # Convert the list of characters back to a string and return the password
    return ''.join(pwd)

# Prompt the user for the minimum password length and desired character types
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers in your password (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters in your password (y/n)? ").lower() == "y"

# Generate the password based on the user's preferences
pwd = generate_password(min_length, has_number, has_special)

# Print the generated password
print(f"The generated password is: {pwd}")
