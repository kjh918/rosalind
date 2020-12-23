import sys
import os
from Bio import SeqIO
from Bio.Seq import Seq
import re

f = sys.argv[1]
data = []
with open(f,'r') as handle:
    for i in handle:
        i  = i.replace('\n','')
        data.append(i)
print(data)
print(str(Seq(data[0]).translate()))

p1 = "(?=(ATG))"
for i in range(len(data)):
    t = []
    xx = [match.start() for match in re.finditer(p1,data[i])]

stop = ['TGA','TAG','TAA']
aa1 = []
for i in xx:
    for n in range(i,len(data[0]),3):
        if data[0][n:n+3] in stop:
            dna = Seq(data[0][i:n+3]).translate()
            aa1.append(str(dna).replace('*',''))
            break
        
r_data = data[0][::-1]
seq_d = {'A':'T','T':'A','G':'C','C':'G'}
r_d = ''
for i in r_data:
    r_d += seq_d[i] 
            
p2 = "(?=(ATG))"
t = []
xx = [match.start() for match in re.finditer(p2,r_d)]

stop = ['TGA','TAG','TAA']
aa2 = []
for i in xx:
    for n in range(i,len(r_d),3):
        if r_d[n:n+3] in stop:
            dna = Seq(r_d[i:n+3]).translate()
            aa2.append(str(dna).replace('*',''))
            break
aa = set(aa1)|set(aa2)
lene = [len(i) for i in list(aa)]

for i in list(aa):
    if len(i) == max(lene):
        print(i)
    
    



