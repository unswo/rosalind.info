'''Problem

Given: Two positive integers a
and b (a<b<10000).

Return: The sum of all odd integers from a
through b, inclusively.'''
# range limit
x = 4676
y = 9236

# inclusively so y+1
list_to_sum = list(range(x, y+1))
# add values if true to z
z = 0
for x in list_to_sum:
    # sum if odd
    if x % 2 == 1:
        z += x
print(z)
