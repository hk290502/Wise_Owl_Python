
denominator = 1
positive = True
total = 0

for i in range(100000):
    if positive:
        total += 1/denominator
    else:
        total -= 1/denominator

    denominator += 2
    positive = not positive


print(total*4)

