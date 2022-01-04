#!/usr/bin/python3

"""
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

    An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
    An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....

You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
"""
from collections import defaultdict

vlines = []
hlines = []
dlines = []
points = []
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
        else:
            dlines.append([(int(x1),int(y1)),(int(x2),int(y2))])

#Fnd all points that fall on diagonal lines
for line in dlines:
    a,b = line
    x1,y1 = a
    x2,y2 = b

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    #e.g. (2,2) -> (7,7)
    if x1 == y1 and x2 == y2:
        d = x2 - x1
        for i in range(0,d):
            points.append((x1+i,y1+i))
        points.append((x2,y2))
        continue
        
    #e.g. (7,1) -> (1,7) or (4,1) -> (0,5) or (2,4) -> (6,8)
    if dx == dy: 
        if x2 > x1:
            _x = [ _ for _ in range(x1,x2) ]
            _x.append(x2)
        elif x1 > x2:
            _x = [ _ for _ in range(x1,x2,-1) ]
            _x.append(x2)

        if y2 > y1:
            _y = [ _ for _ in range(y1,y2) ]
            _y.append(y2)
        elif y1 > y2:
            _y = [ _ for _ in range(y1,y2,-1) ]
            _y.append(y2)

        for point in zip(_x,_y): points.append(point)

#Find all points that fall on vertical lines
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

#assert (798,666) in points
#assert (628,339) in points

#Find all points that fall on horizontal lines
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

#assert (700,444) in points
#assert (376,128) in points

for _ in points:
#    print(_)
    overlapping_points[_] += 1

count = 0
for k in overlapping_points:
    if overlapping_points[k] > 1: count += 1

print('Number of overlapping points', count)
