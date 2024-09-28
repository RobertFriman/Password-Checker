# Function to check if a string contains only ASCII characters
def is_ascii(password):
    try:
        password.encode('ascii')
    except UnicodeEncodeError:
        return False
    return True

# Reading the dataset and filtering passwords with non-ASCII characters
rockyou_file = 'rockyou.txt'
ascii_passwords = []
non_ascii_passwords = []

with open(rockyou_file, 'r', encoding='latin1') as file:  # 'latin1' encoding handles the RockYou dataset encoding
    for password in file:
        password = password.strip()  # Remove leading/trailing whitespace
        if is_ascii(password):
            if password != " ":
                ascii_passwords.append(password)
        else:
            non_ascii_passwords.append(password)

no_duplicates = list(set(ascii_passwords))
no_duplicates.remove('')

# Output results
print(f"Total passwords: {len(ascii_passwords) + len(non_ascii_passwords)}")
print(f"ASCII passwords: {len(ascii_passwords)}")
print(f"No duplicates count: {len(no_duplicates)}")
print(f"Non-ASCII passwords: {len(non_ascii_passwords)}")

# Save filtered passwords
with open('ascii_rockyou.txt', 'w', encoding='utf-8') as ascii_file:
    for pwd in no_duplicates:
        ascii_file.write(pwd + '\n')

with open('non_ascii_rockyou.txt', 'w', encoding='utf-8') as non_ascii_file:
    for pwd in non_ascii_passwords:
        non_ascii_file.write(pwd + '\n')