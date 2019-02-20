num = [1, 4, -5, 10, -7, 2, 3, -1]
filter_and_squared = []

for number in num:
    if number > 0:
        filter_and_squared.append(number ** 2)

print(filter_and_squared)

filter_and_squared1 = [x ** 2 for x in num if x > 0]
print(filter_and_squared1)
