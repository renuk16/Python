#Given a sequence, write a program to detect cycles within it.
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
    	line = test.rstrip("\n").split(" ")
    	x = []
    	count = []
    	for s in line:
    		if s not in x:
    			x.append(s)
    			count.append(line.count(s))
    	for i in range(0,len(x)):
    		if (count[i] > 1):
    			print x[i],
    	print " " 







        