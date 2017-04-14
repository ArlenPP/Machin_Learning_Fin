#today buy today sell

import os
import csv

test_result = open('../../../output/19/test-result','r')
test = open('./test.csv','r')

labels= []
open = []
close = []


for row in csv.DictReader(test_result, delimiter=' '):
	labels.append(float(row['labels']))


for row in csv.DictReader(test):
	open.append(float(row['Open']))
	close.append(float(row['Close']))



for i in range (len(open)-len(labels),len(labels),1):

	
	if(labels[i]==1):
		sumbuy=sumbuy+float(open[i])
		sumsell=sumsell+float(close[i])
	elif(labels[i]==-1):
		sumbuy=sumbuy+float(close[i])
		sumsell=sumsell+float(open[i])


print(sumsell/sumbuy)