#import re
from Bio.Seq import Seq

# Original attempt
with open('rosalind_splc.txt') as file:
    fasta = file.read()

fasta_split = fasta.split('\n')
print(fasta_split)

seq = ''
for x in fasta_split[1:]:
    if x.count('>') == 0:
        seq += x
        fasta_split.remove(x)
    if x.count('>') > 0:
        break
print(seq)
print(fasta_split)
introns = fasta_split[2::2]
print(introns)

for x in introns:
    exon = seq.split(x)
    seq = ''.join(exon)
print(seq)

print(Seq(seq).translate(to_stop=True))