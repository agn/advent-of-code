#!/usr/bin/python3

"""
To do this, count the number of times a depth measurement increases from the previous measurement. (There is no measurement before the first measurement.) In the example above, the changes are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)

In this example, there are 7 measurements that are larger than the previous measurement.

How many measurements are larger than the previous measurement?
"""

with open('input', 'r') as input:
    measurements = list(map(int, input.readlines()))

count_larger = 0
prev_measurement = measurements[0]

for current in measurements[1:]:
    if current > prev_measurement: count_larger += 1
    prev_measurement = current

print(count_larger)
