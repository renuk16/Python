import collections
dict2010 = collections.defaultdict(float)
dict2100 = collections.defaultdict(float)
diff = collections.defaultdict(float)

with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = float(line[5])
	line[6] = float(line[6])
        if line[1] == 'Total National Population':
		print line
		dict2010[line[0]] += line[5]
		dict2100[line[0]] += line[6]
            	diff[line[0]] =  dict2100[line[0]] - dict2010[line[0]]

z = dict((k, float(diff[k]) / dict2010[k] ) for k in diff)

with open('national_population.csv', 'w') as outputFile:
    outputFile.write('continent,90 year population increase\n')

    for k, v in z.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')
