import sys
from itertools import permutations

f = sys.argv[1]

f = int(f)

items = []
for i in range(f+1):
    if i == 0:
        continue
    items.append(i)
    items.append(-i)
x = list(permutations(items,f))

result = []
for i in range(len(x)):
    cc = 0
    for j in range(0,f):
        if -x[i][j] not in x[i]:
            cc += 1
            if cc == f:
                result.append(x[i])
                cc = 0

print(len(result))
for i in result:
    print(*i,sep=' ')


