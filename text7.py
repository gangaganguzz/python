fruits = ["apple","orange","mango"]
vegetables = ["tomato","Potato","onion"]
beverages = ["water","juice","milk"]
fruits.append("Mango")
vegetables.insert(1,"Carrot")
beverages.pop()
inventory = [fruits, vegetables, beverages]
print(fruits[:2])
print(vegetables[-1])
fruit_lengths = [len(item) for item in fruits]
print(fruit_lengths)
print("water" in beverages)
first_items = (fruits[0], vegetables[0], beverages[0])
print(first_items)
print(inventory)
