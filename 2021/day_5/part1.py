#!/usr/bin/python3

"""
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

    An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....

In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
"""
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

