import random
import string

length = int(input("Enter password length: "))

letters = string.ascii_letters      # a-z + A-Z
numbers = string.digits             # 0-9
symbols = string.punctuation        # !@#$%^&* etc.

all_characters = letters + numbers + symbols

# Generate password
password = ""

for i in range(length):
    password += random.choice(all_characters)

print("\nGenerated Password:")
print(password)