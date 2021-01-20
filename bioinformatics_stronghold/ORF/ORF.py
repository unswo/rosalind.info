from Bio.Seq import Seq
import itertools as re

dna = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
rev_dna = dna[::-1]

def find_orf(str):
    re.

dna = Seq(dna)
rev_dna = Seq(rev_dna)

frame_1 = dna
frame_2 = dna[1:-2]
frame_3 = dna[2:-1]
frame_4 = rev_dna
frame_5 = rev_dna[1:-2]
frame_6 = rev_dna[2:-1]

#frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6]
#frames = [x.translate(to_stop=True) for x in frames]

#print([len(x) % 3 for x in frames])

print(frame_1)