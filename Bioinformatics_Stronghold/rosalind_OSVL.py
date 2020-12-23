import sys
from itertools import permutations
import itertools

f = sys.argv[1]

result = []
with open(f,'r') as handle:
    for line in handle:
        line = line.replace('\n','')
        result.append(line.split(' '))
a = [int(i) for i in result[1]]
a = a[0]
tex_list = result[0]
#print(tex_list)
#print(a)
re = []
num = 0
for i in range(len(tex_list)):
    re.append(tex_list[i])
    for j in range(len(tex_list)):
        re.append(tex_list[i]+tex_list[j])
        for k in range(len(tex_list)):
            re.append(tex_list[i]+tex_list[j]+tex_list[k])
            for m in range(len(tex_list)):
                re.append(tex_list[i]+tex_list[j]+tex_list[k]+tex_list[m])
print(*re,sep='\n')




'''
leg = []
for i in range(1,a+1):
    x = list(permutations(result[0],i))
    for j in range(len(x)):
        b = ''
        for k in range(i):
            b += x[j][k]
        leg.append(b)
leg_1 = sorted(leg)

for i in leg_1:
    print(i)
'''
'''
re = []
for i in range(1,a+1):
    kk = [''.join(p) for p in itertools.product(result[0],repeat=i)]
    [re.append(j) for j in kk]

print(re)
ax = []
for i in result[0]:
    for j in re:
        if j.startswith(i):
            ax.append(j)
for i in ax:
    print(i)
 ''' 


