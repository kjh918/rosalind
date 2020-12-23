import sys

f = sys.argv[1]

x = []
with open(f,'r') as handle:
    for line in handle:
        a = line.replace('\n','')
        x.append(a)
y = x[1:]

print(x[0])
print(y)

num_list = []
for i in y:
    k = y.split(' ')
    num_list.append(k)

print(num_list)
