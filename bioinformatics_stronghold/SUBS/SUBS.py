
string = 'CTGCCGGCTGCCGGCTGCCGGACTGCCGGCTGCCGGACCTGCCGGACTGCCGGGTGCACTGCCGGCTGCCGGCTGCCGGGCAACTGCCGGTGGTGCTGCCGGCCCGCTGCCTGCCGGACAGTGACCTGCCGGTTCTCTGCCGGACTGCCGGTACTGCCGGCTGCCGGTATGCACTGCCGGATCTGCCGGACTGCCGGACTGCCGGATCAGCCTGCCGGTCCTGCCGGACTGCCGGCTGCCGGACTGCCGGGCCTGCCGGCGCTGCCGGTTCATCCTCTGCCGGACTGCCGGGGCTGCCGGACTCCGTCTGCCGGTACTGCCGGTATCCTGCCGGTACGTACCTGCCGGAGGAGAGGCTGCCGGATCGCTGCCGGCTGCCGGTTGCTGCCGGTAGGCTGCCGGAAGTGCTGCCGGGGACTGCCGGTTCTGGCGGCTGCCGGGCTCTGCCGGCTGCCGGTCTAACCTGCCGGCTGCCGGCTAACTGCCGGACTGCCGGCGTGGCTGCCGGCGATCTGCCGGGCTGCCGGCCCTGCCGGCCCTTCACTGCCGGACACGGCCCTGCCGGTCTGCCGGCCTGCTGCCGGCTGCCGGACTGCCGGCAACTGCCGGTACTGCCGGCTGCCGGCAACTGCCGGCCCTGCCGGGCCTGCCGGCTGCCGGGACTCTGCCGGCTGCCGGGGATGCTGCCGGCCAGCACTGCCGGCCTGCCGGGTTTGGTGACTGCCGGCTGCCGGCTGCCGGGCCTGCCGGCCTGCCGGACTGCCGGCCTATGGCTGCCGGTCCCGCTGCCGGCTGCCGGCTGTCCTGCCGGTCTGCCGGGCTGCCGGTGCACAAAGACTGCCGGCTGCCGGATCTGCCGGGACTGCCGGGACTGCCGGAACTTATCCTGCCGG'
sub = 'CTGCCGGCT'
string_loc = ''

for x in range(len(string)):
    if string[x:x+len(sub)] == sub:
        string_loc += str(x+1) + ' '

print(string_loc)
