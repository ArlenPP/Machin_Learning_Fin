import os
import csv

tmp_call = csv.DictReader(open('./merge_call/test-result','r'),delimiter=' ')
tmp_put = csv.DictReader(open('./merge_put/test-result','r'),delimiter=' ')

label_call = []
label_put = []
zero_possible = []
call_possible = []
put_possible = []

for row in tmp_call:
	label_call.append(row['labels'])
	zero_possible.append(row['0'])
	call_possible.append(row['1'])

for row in tmp_put:
	label_put.append(row['labels'])
	put_possible.append(row['-1'])

f = open('./test-result','w')

f.write('labels 0 1 -1\n')

for i in range(len(label_call)):
	if(label_call[i] == '1' and (label_put[i] == '1' or label_put[i] == '0')):
		f.write(str(label_call[i])+' '+str(zero_possible[i])+' '+str(call_possible[i])+' '+str(put_possible[i])+'\n')
	elif(label_put[i] == '-1' and (label_call[i] == '-1' or label_call[i] == '0')):
		f.write(str(label_put[i])+' '+str(zero_possible[i])+' '+str(call_possible[i])+' '+str(put_possible[i])+'\n')
	else:
		f.write('0 0.98 0.01 0.01\n')

