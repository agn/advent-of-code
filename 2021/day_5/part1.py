#!/usr/bin/python3
from collections import defaultdict

vlines = []
hlines = []
overlapping_points = defaultdict(int)

#Find only the vertical and horizontal lines
with open('input', 'r') as input:
    for line in input.read().splitlines():
        a, b = line.split(' -> ')
        x1,y1 = a.split(',')
        x2,y2 = b.split(',')
        if x1 == x2: 
            vlines.append([(int(x1),int(y1)),(int(x2),int(y2))])
        elif y1 == y2:
            hlines.append([(int(x1),int(y1)),(int(x2),int(y2))])

points = []
#Find all points vertical lines fall on
for line in vlines:
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

#Find all points horizontal lines fall on
for line in hlines:
    a,b = line
    x1,y = a
    x2,y = b
    if x2 > x1:
        for x in range(x1,x2):
            points.append((x,y))
        points.append((x2,y))
    elif x1 > x2:
        for x in range(x1,x2,-1):
            points.append((x,y))
        points.append((x2,y))

assert (700,444) in points
assert (376,128) in points

for _ in points:
    overlapping_points[_] += 1

count = 0
for k in overlapping_points:
    if overlapping_points[k] > 1: count += 1

print('Number of overlapping points', count)

