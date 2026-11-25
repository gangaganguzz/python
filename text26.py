import random
import math

names = input("Enter customer names separated by commas: ")

name_list = names.split(",")

unique_names = list(set(name_list))

random.shuffle(unique_names)

winners = random.sample(unique_names, 2)

winner1 = winners[0][::-1]
winner2 = winners[1][::-1]

total_participants = len(unique_names)

square_root = round(math.sqrt(total_participants))

print("Shuffled names:", unique_names)
print("Winner 1:", winner1)
print("Winner 2:", winner2)
print("Total unique participants:", total_participants)
print("Rounded square root:", square_root)