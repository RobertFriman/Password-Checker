import secrets
import string
import random

def generate_strong_password(min_length=12, max_length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    length = random.randint(min_length, max_length)  # Random length between min_length and max_length
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Generate 14,329,222 strong passwords with varying lengths (e.g., between 12 and 20 characters)
strong_passwords = [generate_strong_password() for _ in range(14329222)]

# Save to a file
with open("strong_passwords.txt", "w", encoding='utf-8') as file:
    for pwd in strong_passwords:
        file.write(pwd + "\n")

print("Generated 14,329,222 strong passwords with varying lengths.")