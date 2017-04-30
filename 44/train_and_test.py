import os
import csv


Open = []
Close = []
High = []
Low = []
BBandMA2 = []
RSI6 = []
RSI12 = []
ADX2 = []
three_openposition = []
openposition = []
price_close= []
price_open = []
price_high = []
price_low = []

dowfile = csv.DictReader(open('./train.csv','r'))

for row in dowfile:
	Open.append(str(float(row['Open'])))
	Close.append(str(float(row['Close'])))
	High.append(str(float(row['High'])))
	Low.append(str(float(row['Low'])))
	BBandMA2.append(str(float(row['BBandMA2'])))
	RSI6.append(str(float(row['RSI6'])))
	RSI12.append(str(float(row['RSI12'])))
	ADX2.append(str(float(row['ADX2'])))
	three_openposition.append(float(row['three_openposition']))
	openposition.append(float(row['openposition']))
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))
	price_high.append(float(row['High']))
	price_low.append(float(row['Low']))



file = open('../../../output/44/train-data','w')
#file = open('./train-data','w')

for day in range(1,len(Open),1):

	if price_close[day]>(price_open[day]):
		a='1'
	elif (price_close[day])<=price_open[day]:
		a='-1'
	else :
		a='0'
	file.write(a)

	number = 0

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Open[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Close[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+BBandMA2[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(Close[i]>float(BBandMA2[i])):
			label=1
		else:
			label=-1
		file.write(' '+b+':'+str(label))

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSI6[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSI12[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(float(RSI12[i])>float(RSI6[i])):
			label=1
		else:
			label=0
		file.write(' '+b+':'+str(label))

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+ADX2[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(float(ADX2[i])>0.59):
			label=1
		else:
			label=0
		file.write(' '+b+':'+str(label))

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+three_openposition[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(three_openposition[i]>0):
			label=1
		else:
			label=-1
		file.write(' '+b+':'+str(label))

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+openposition[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(openposition[i])>0:
			label=1
		else:
			label=-1
		file.write(' '+b+':'+str(label))

	file.write('\n')
file.close()




Open = []
Close = []
High = []
Low = []
BBandMA2 = []
RSI6 = []
RSI12 = []
ADX2 = []
three_openposition = []
openposition = []
price_close= []
price_open = []
price_high = []
price_low = []

dowfile2 = csv.DictReader(open('./test.csv','r'))

for row in dowfile2:
	Open.append(str(float(row['Open'])))
	Close.append(str(float(row['Close'])))
	High.append(str(float(row['High'])))
	Low.append(str(float(row['Low'])))
	BBandMA2.append(str(float(row['BBandMA2'])))
	RSI6.append(str(float(row['RSI6'])))
	RSI12.append(str(float(row['RSI12'])))
	ADX2.append(str(float(row['ADX2'])))
	three_openposition.append(float(row['three_openposition']))
	openposition.append(float(row['openposition']))
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))
	price_high.append(float(row['High']))
	price_low.append(float(row['Low']))


file2 = open('../../../output/44/test-data','w')
#file2 = open('./test-data','w')



for day in range(1,len(Open),1):

	if price_close[day]>(price_open[day]):
		a='1'
	elif (price_close[day])<=price_open[day]:
		a='-1'
	else :
		a='0'
	file2.write(a)

	number = 0
	
	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+Open[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+Close[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+BBandMA2[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(Close[i]>float(BBandMA2[i])):
			label=1
		else:
			label=-1
		file2.write(' '+b+':'+str(label))

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+RSI6[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+RSI12[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(float(RSI12[i])>float(RSI6[i])):
			label=1
		else:
			label=0
		file2.write(' '+b+':'+str(label))

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+ADX2[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(float(ADX2[i])>0.59):
			label=1
		else:
			label=0
		file2.write(' '+b+':'+str(label))

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+three_openposition[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(three_openposition[i]>0):
			label=1
		else:
			label=-1
		file2.write(' '+b+':'+str(label))

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+openposition[i])

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(openposition[i])>0:
			label=1
		else:
			label=-1
		file2.write(' '+b+':'+str(label))

	file2.write('\n')
file2.close()

