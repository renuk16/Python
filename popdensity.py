'''
Try and calculate the population density (total national population divided by the total land area and remember to convert at least one number to float). Which continent was most densely populated in 2010?
'''

import collections
pop = collections.defaultdict(float)
area = collections.defaultdict(float)
population_dict = collections.defaultdict(float)

with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = float(line[5])
	line[7] = float(line[7])
        if line[1] == 'Total National Population':
            pop[line[0]] += line[5]
	    area[line[0]] += line[7]

print pop
print area

z = dict((k, float(pop[k]) / area[k] ) for k in pop)

print z

with open('national_population.csv', 'w') as outputFile:
    outputFile.write('continent,popdensity\n')

    for k, v in z.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')
