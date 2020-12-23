import sys
from Bio import SeqIO

f = sys.argv[1]

seq = SeqIO.parse(f,'fastq')
num = 22
total = 0
for i in seq:
    k = i.letter_annotations['phred_quality']
    if  num > sum(k)/len(k):
        print(sum(k)/len(k))
        total += 1
print(total)
