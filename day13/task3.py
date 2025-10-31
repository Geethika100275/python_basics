import random
import string

print("🔐 Advanced Password Generator 🔐")


length = int(input("Password length (8-50): "))
include_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
exclude_similar = input("Exclude similar characters (0,O,l,1)? (y/n): ").lower() == 'y'


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

chars = lowercase
if include_upper:
    chars += uppercase
if include_numbers:
    chars += numbers
if include_symbols:
    chars += symbols


if exclude_similar:
    for ch in "0Ol1":
        chars = chars.replace(ch, "")
if length < 8 or length > 50:
    print("Password length must be between 8 and 50. Using default length 12.")
    length = 12
password = ''.join(random.choice(chars) for _ in range(length))
strength_points = 0
if len(password) >= 12:
    strength_points += 1
if any(c.isupper() for c in password):
    strength_points += 1
if any(c.islower() for c in password):
    strength_points += 1
if any(c.isdigit() for c in password):
    strength_points += 1
if any(c in symbols for c in password):
    strength_points += 1

if strength_points <= 2:
    overall_strength = "Weak"
elif strength_points == 3 or strength_points == 4:
    overall_strength = "Moderate"
else:
    overall_strength = "Strong"


print("\nGenerated password:", password)
print("\nPassword Analysis:")
print(f"Length: {'Strong' if len(password) >= 12 else 'Weak'} ({len(password)} characters)")
print(f"Uppercase: {'Yes' if any(c.isupper() for c in password) else 'No'}")
print(f"Lowercase: {'Yes' if any(c.islower() for c in password) else 'No'}")
print(f"Numbers: {'Yes' if any(c.isdigit() for c in password) else 'No'}")
print(f"Symbols: {'Yes' if any(c in symbols for c in password) else 'No'}")
print(f"Overall strength: {overall_strength}")
