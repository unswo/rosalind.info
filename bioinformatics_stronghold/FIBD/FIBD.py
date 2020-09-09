n = 94
m = 16

# create list to track ages of rabbits
ages = [0] * m
# intitalise single pair of rabbits
ages[-1] = 1
# 1 to n months
for i in range(1, n):
    # one pair produced from each pair
    babies = sum(ages[:-1])
    ages[:-1] = ages[1:]
    ages[-1] = babies

print(sum(ages))


