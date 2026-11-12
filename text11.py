
attendance = [18, 20, 19, 15, 21]

full_days = 0
total = 0

for x in attendance:
    if x >= 20:
        print("Full")
        full_days += 1
    else:
        print("Not Full")

    total += x

print("Full days:", full_days)
print("Total attendance:", total)