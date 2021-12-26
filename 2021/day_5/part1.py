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

print('Horizontal lines:', len(hlines), hlines)
print('Vertical lines:', len(vlines), vlines)
points = []
intersection = 0

for line in vlines:
    #print('vline>>', line)
    a,b = line
    x,y1 = a
    x,y2 = b

    if y2 > y1:
        for y in range(y1,y2):
            points.append((x,y))
        points.append((x,y2))
    elif y1 > y2:
        for y in range(y1,y2,-1):
            points.append((x,y))
        points.append((x,y2))

assert (798,666) in points
assert (628,339) in points
print('Points', points, len(points))

hpoints = []
for line in hlines:
    #print('hline >>', line)
    a,b = line
    x1,y = a
    x2,y = b
    if x2 > x1:
        for x in range(x1,x2):
            hpoints.append((x,y))
        hpoints.append((x2,y))
    elif x1 > x2:
        for x in range(x1,x2,-1):
            hpoints.append((x,y))
        hpoints.append((x2,y))

print(hpoints, len(hpoints))
print('Intersections:', intersection)
assert (700,444) in hpoints
assert (376,128) in hpoints
