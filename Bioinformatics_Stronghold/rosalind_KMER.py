import sys
import os
import re
import itertools
from Bio import SeqIO
f = sys.argv[1]

mer = ['A','C','G','T']
mer4 = [''.join(p) for p in itertools.product(mer,repeat=4)]
seq_list = []
seq = SeqIO.parse(f,'fasta')
for i in seq:
    seq_list.append(i.seq)

#print(seq_list[0])
a = str(seq_list[0])
y = []
for i in range(len(mer4)):
    xx = [match.start() for match in re.finditer(mer4[i],a)]
    for v in range(1,4):
        for j in xx:
            if a[j+v:j+v+4] == mer4[i]:
                xx.append(j+v)
    y.append(str(len(set(xx))))
print(*y,sep= ' ')
'''
kk = []
for i in mer4:
    a = str(seq_list[0]).find(i)
    if a >= 0:
        kk.append(a)
        for j in range(a,len(seq_list[0])-4):
            dd = str(seq_list[0][j]).find(i)


print(*kk,sep=' ')
'''

