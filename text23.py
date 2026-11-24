item = input("Enter a new item: ")

with open("items.txt", "a+") as file:
    file.write(item + "\n")

    file.seek(0)
    print("Full list of items:")
    print(file.read())
