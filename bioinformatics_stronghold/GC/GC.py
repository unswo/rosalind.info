with open('rosalind_gc.txt') as FA:
    FA = FA.readlines()

FA = [x.rstrip() for x in FA]
FA = ''.join(FA)
FA = FA.split('>')
FA = FA[1:]

di = {}
i = 0
for i in FA:
    di[i[0:13]] = i[13:]

di_total = {}

for key, value in di.items():
    key = key.strip('>')
    di_total[key] = (value.count('G') + value.count('C')) * 100 / len(value)

big_val = max(di_total, key=di_total.get)
print(big_val, '\n', di_total[big_val])
