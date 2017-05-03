import os

def howmuchone(f):
	number0 = 0.0
	number1 = 0.0
	numberminus1 = 0.0
	total = 0.0
	with open(f,'r') as file:
		line = file.readlines()
		for i in (line):
			total += 1
			if i[0] == '0':
				number0 += 1
			elif i[0] == '1':
				number1 +=1
			elif i[0] == '-':
				numberminus1 += 1
			else:
				print("no~~~~~~~~~~~~~~~~~~~")
		print("number of 0 = "+str(number0)+' '+str(number0/total))
		print("number of 1 = "+str(number1)+' '+str(number1/total))
		print("number of -1 = "+str(numberminus1)+' '+str(numberminus1/total))
		print("total = "+str(total))


f = './train-data'
howmuchone(f)