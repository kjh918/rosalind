import sys
import Bio
import re
from Bio import SeqIO

f = sys.argv[1]

seq = SeqIO.parse(f,'fasta')

seq_list = []
for i in seq:
    seq_list.append(str(i.seq))
print(seq_list)


a = []
for i in seq_list:
    xx = []
    xx = [[match.start(), match.end()] for match in re.finditer(i,seq_list[0])]
    if len(xx) !=0:
        for j in xx:
            a.append(j)
print(a)

print(re.match(seq_list[0],seq_list[1]))
