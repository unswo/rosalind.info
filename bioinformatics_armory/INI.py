

seq = "GGGTCCAACACTAAAGATGACAACGAATTCTAAATGTTGTGCTGGGGTGAAACCTCATGCGTGAACATTGTGCAAGGGTTTTACCCGGTCTAGAGCCTGAAATCTTCGCCGGGGTCCCTTATAATTCCTTGGTCCCATGTGGATGCAACACCGCTCGGTAATATAAACGTTGGGCCGCAATTAGCGGTAGAATTCCACTAATAAGGCACTATTTGTTTGGATCAAACGTTATGCGAATATTAGCAATGACCGCCACTCTGGCTAAATTGTACATTAGAGTCCTCATTAAAGGTACGGTGTCTGTTACTTTTTTCTTGGCCGTTGGCGTACAGGATGGCGCTCAGTCACAGACAGCCTCTCAAGTCGCGACATCCTTGACATCGCAACAGGTGCGGTTCTGCTGTCATGATGTAACCAATGTGTCGCCTATGCAGTCCTAGGACGGTGTAGATCTGGCAGCCAACCCGAGGAGGCCCTAACCCTTGAGCTACCGCCCTTATATTATAGGTTCCCAGTCAAGCCTGGTTAACACCATAAGACCTCCTGGGATGGCGTCGTAGACTTCGGGGCCTTAAATGGCTTAAGCATGGTCATATGCGCATAGATTCACAGGTTCAGACATAGGGAGGACTCAACGTTCCTTGTACGTTTGAAGCAATAAGCTTTACACATAGGACTTCCTTGTCCGCCAAGGTCCAATCCAAACGGAACAAGTTGGACACTAAACCTGGTGCTTCAGCAGACTCCATTAACGGTGGGGTGCCACCTCCTTACCTGTTCCGTTCGTTGGTCGCAAACGTATTTAACTGAGCTCGGTGAGTATACCCTGACGTCAGGAGCAGACCACCTCGACTGATAGAGCAGGTCGGACGATTAGGAGCATAGACTATAGTGGCTAAGCGACTTTCATAGAGATCGTTGTTAAACCAATGGTCTGTTCTACGCCTTTAAGACTCCTATGTCCTCAGGG"


def count_nuc(seq):
    seq_dict = {'A': seq.count('A'), 'C': seq.count('C'), 'G': seq.count('G'),
                'T': seq.count('T')}
    print(seq_dict)
