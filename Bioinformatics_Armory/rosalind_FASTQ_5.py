import sys
from Bio import SeqIO
import numpy as np
import pandas as pd

f = sys.argv[1]
num  = []
with open(f,'r') as handle:
    for line in handle:
        num.append(line)
with open('fastq_data.txt','w') as handle:
    handle.writelines(num[1:])

seq = SeqIO.parse('fastq_data.txt','fastq')
x = []
y = []
for i in seq:
    y.append(i.letter_annotations['phred_quality'])
    x.append(str(i.seq))

result = []
for s in range(len(y)):
    if pd.Series(y[s]).quantile(.75) - pd.Series(y[s]).quantile(.25) < 10:
        print(pd.Series(y[s]).quantile(.75) - pd.Series(y[s]).quantile(.25))
        print(np.median(np.array(y[s])))
        for i in y[s]:
            if i < int(num[0]):
                result.append(i)

print(round(sum(result)/len(result)))


