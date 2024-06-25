import random
import string

def generate_password(length:int):
    required_len = 8
    if length < required_len:
        raise ValueError("Password length must be at least 8 characters long")

    # Generate one character of each required type
    capital_letter = random.choice(string.ascii_uppercase)
    special_char = random.choice(string.punctuation)
    number = random.choice(string.digits)
    
    # Generate the remaining characters
    remaining_length = length - required_len
    all_characters = string.ascii_letters + string.digits + string.punctuation
    remaining_chars = random.choices(all_characters, k=remaining_length)
    
    # Combine all characters and shuffle them
    password_list = [capital_letter, special_char, number] + remaining_chars
    random.shuffle(password_list)
    
    # Convert the list to a string and return
    password = ''.join(password_list)
    return password
