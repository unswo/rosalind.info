'''Problem

Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.'''
file = 'rosalind_ini5.txt'
with open(file) as y:
    z = y.readlines()
    # remove newlines etc
    z = [z.rstrip() for z in z]
    # starts at line 2, skips every other line
    z = z[1::2]
    # join separated by newlines 
    z = '\n'.join(z)
    print(z)