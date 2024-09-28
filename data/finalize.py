import csv

strongs = []
weaks = []

# Read strong passwords
with open("strong_passwords.txt", "r") as strong:
    for pwd in strong:
        strongs.append(pwd.strip())  # Strip newline characters

# Read weak passwords
with open("ascii_rockyou.txt", "r") as weak:
    for pwd in weak:
        weaks.append(pwd.strip())  # Strip newline characters

# Save dataset with CSV module
with open("dataset.csv", "w", newline='') as dataset:
    writer = csv.writer(dataset)
    writer.writerow(["password", "label"])  # Header row
    for i in range(len(strongs)):
        writer.writerow([strongs[i], "strong"])
        writer.writerow([weaks[i], "weak"])

print("Dataset saved successfully!")