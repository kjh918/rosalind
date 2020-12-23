import sys

f = int(sys.argv[1])
a = 0
b = 1
c = 0
x = 1

while x <= f:
    c = a+b
    b = a
    a = c
    x += 1
print(c)

