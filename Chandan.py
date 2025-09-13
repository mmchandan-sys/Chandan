uoa=int(input("Enter the first number: "))
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


#✨simple to-Do list App

tasks = []

while True:
    print("\n📋 To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("✅ Task added!")
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
    elif choice == "3":
        print("Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice, try again.")
