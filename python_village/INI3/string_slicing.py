'''Problem

Given: A string s
of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a
through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.'''

y = open('rosalind_ini3-1.txt')
x = y.readlines()
x = [x.rstrip() for x in x]

str = x[0]
x = x[1].split(' ')
x = [int(x) for x in x]
# plus 1 as indices are inclusive
print(str[x[0]:x[1]+1] + ' ' + str[x[2]:x[3]+1])