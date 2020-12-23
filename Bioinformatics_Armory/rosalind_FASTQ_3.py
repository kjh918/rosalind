import sys
from Bio.Seq import translate

f = sys.argv[1]

x = []
with open(f,'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        x.append(line)

for i in range(1,7):
    a_seq = translate(x[0],table = i,to_stop=True,stop_symbol = '*')
    if a_seq  == x[1]:
        print(i)
for i in range(9,17):
    a_seq = translate(x[0],table = i,to_stop=True,stop_symbol = '*')
    if a_seq  == x[1]:
        print(i)
for i in range(21,24):
    a_seq = translate(x[0],table = i,to_stop=True,stop_symbol = '*')
    if a_seq  == x[1]:
        print(i)

