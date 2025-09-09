a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a >= b and a >= c:
    print(a, "is the largest number")
elif b >= a and b >= c:
     print(b, "is the largest number")
else:
    print(c, "is the largest number")



#📌 Password Generator

import random
import string

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔐 Random Password Generator")
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
