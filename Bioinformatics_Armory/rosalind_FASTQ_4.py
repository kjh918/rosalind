import sys
from Bio import SeqIO

f = sys.argv[1]
num  = []
fastq = []
with open(f,'r') as handle:
    for line in handle:
        num.append(line)
with open('fastq_data.txt','w') as handle:
    handle.writelines(num[1:])

seq = SeqIO.parse('fastq_data.txt','fastq')

y = []
for i in seq:
    y.append(i.letter_annotations['phred_quality'])

lim = num[0].replace('\n','')
lim = lim.split(' ')
print(lim)

lim[0]

result = 0
for s in range(len(y)):
    total = 0
    for i in y[s]:
        if i >= int(lim[0]):
            total += 1
 #   print(total/len(y[s]))
    if total/len(y[s]) >= int(lim[1])/100:
        result += 1

print(result)
