#!/usr/bin/python3

vlines = []
hlines = []
with open('input', 'r') as input:
    for line in input.read().splitlines():
        a, b = line.split(' -> ')
        x1,y1 = a.split(',')
        x2,y2 = b.split(',')
        if x1 == x2: 
            vlines.append([(int(x1),int(y1)),(int(x2),int(y2))])
        elif y1 == y2:
            hlines.append([(int(x1),int(y1)),(int(x2),int(y2))])

#print('Horizontal lines:', len(hlines), hlines)
print('Vertical lines:', len(vlines))

for line in vlines:
    print('>>', line)
    a,b = line
    x,y1 = a
    x,y2 = b

    if y2 > y1:
        for y in range(y1,y2):
            if y != y1: line.append((x,y))
    elif y1 > y2:
        for y in range(y1,y2,-1):
            if y != y1: line.append((x,y))
    print('<<', line)
    break

print('Vertical lines:', len(vlines))
