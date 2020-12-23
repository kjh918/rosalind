# rosalind_lgis.txt
import sys
import numpy as np 

f = sys.argv[1]

num_list = []
with open(f,'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        num_list.append(line.split(' '))    
x = []
for i in num_list:
    for j in i:
        x.append(int(j))

x1 = x[:30]
'''
i_count = {}
d_count = {}
for i in range(len(x1)):
    if i == 0:
        i_count[x1[i]] = 1
        d_count[x1[i]] = 1
    elif max(list(i_count.keys())) < x1[i]:
        i_count[x1[i]] = max(i_count.keys())+1
    elif max(i_count.keys()) > x1[i]:
        i_count[x1[i]] = max(i_count.keys()< x1[i]) +1

print(i_count)
'''
d = {1:2,2:3,4:5,6:8,3:2}
print(max(list(d.keys())) < 5)
