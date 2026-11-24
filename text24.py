count = int(input("How many student names do you want to add? "))

try:
    with open("students.txt", "r") as file:
        print("Existing student names:")
        print(file.read())

except FileNotFoundError:
    print("File does not exist yet.")

with open("students.txt", "a") as file:
    for i in range(count):
        name = input("Enter student name: ")
        file.write(name + "\n")

with open("students.txt", "r") as file:
    print("\nUpdated student list:")
    print(file.read())