import os
import csv


Open = []
High = []
Low = []
Close = []
BBandMA2 = []
Di2add = []
Di2minus = []
ADX2 = []
RSI6 = []
RSI12 = []
three_openposition = []
openposition = []
SMA5 = []
SMA10 =[]
Volume = []
MA5 = []
MA10 = []
DIF12 = []
MACD9 = []
OSC = []
K = []
D = []
AR10 = []
RSV5 = []
price_close= []
price_open = []
price_high = []
price_low = []

dowfile = open('./train.csv','r')

for row in csv.DictReader(dowfile):
	Open.append(str(float(row['Open'])))
	High.append(str(float(row['High'])))
	Low.append(str(float(row['Low'])))
	Close.append(str(float(row['Close'])))
	BBandMA2.append(str(float(row['BBandMA2'])))
	Di2add.append(str(float(row['Di2add'])))
	Di2minus.append(str(float(row['Di2minus'])))
	ADX2.append(str(float(row['ADX2'])))
	RSI6.append(str(float(row['RSI6'])))
	RSI12.append(str(float(row['RSI12'])))
	three_openposition.append(float(row['three_openposition']))
	openposition.append(float(row['openposition']))
	SMA5.append(str(float(row['SMA5'])))
	SMA10.append(str(float(row['SMA10'])))
	Volume.append(str(float(row['Volume'])))
	MA5.append(str(float(row['MA5'])))
	MA10.append(str(float(row['MA10'])))
	DIF12.append(str(float(row['DIF12'])))
	MACD9.append(str(float(row['MACD9'])))
	OSC.append(str(float(row['OSC'])))
	K.append(str(float(row['K'])))
	D.append(str(float(row['D'])))
	AR10.append(str(float(row['AR10'])))
	RSV5.append(str(float(row['RSV5'])))
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))
	price_high.append(float(row['High']))
	price_low.append(float(row['Low']))
dowfile.close()


#file = open('../../../output/45/train-data','w')
file = open('./train-data','w')

for day in range(5,len(Open),1):

	if price_close[day]>price_open[day]:
		a='1'
	elif price_close[day]<=price_open[day]:
		a='-1'
	else :
		a='0'
	file.write(a)

	number = 0
	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Open[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Close[i])
		'''
	for i in range(day-1,day-3,-1):
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

	for i in range(day-1,day-3,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Di2add[i])

	for i in range(day-1,day-3,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Di2minus[i])

	for i in range(day-1,day-3,-1):
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

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSI6[i])

	for i in range(day-1,day-6,-1):
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

	for i in range(day-1,day-3,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+str(three_openposition[i]))

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(three_openposition[i]>0):
			label=1
		else:
			label=-1
		file.write(' '+b+':'+str(label))

	for i in range(day-1,day-3,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+str(openposition[i]))

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(openposition[i])>0:
			label=1
		else:
			label=-1
		file.write(' '+b+':'+str(label))
		'''
	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA5[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA10[i])
	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Volume[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MA5[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MA10[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+DIF12[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MACD9[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+OSC[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+K[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+D[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+AR10[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSV5[i])

	file.write('\n')
file.close()



Open = []
High = []
Low = []
Close = []
BBandMA2 = []
Di2add = []
Di2minus = []
ADX2 = []
RSI6 = []
RSI12 = []
three_openposition = []
openposition = []
SMA5 = []
SMA10 =[]
Volume = []
MA5 = []
MA10 = []
DIF12 = []
MACD9 = []
OSC = []
K = []
D = []
AR10 = []
RSV5 = []
price_close= []
price_open = []
price_high = []
price_low = []

dowfile2 = open('./test.csv','r')

for row in csv.DictReader(dowfile2):
	Open.append(str(float(row['Open'])))
	High.append(str(float(row['High'])))
	Low.append(str(float(row['Low'])))
	Close.append(str(float(row['Close'])))
	BBandMA2.append(str(float(row['BBandMA2'])))
	Di2add.append(str(float(row['Di2add'])))
	Di2minus.append(str(float(row['Di2minus'])))
	ADX2.append(str(float(row['ADX2'])))
	RSI6.append(str(float(row['RSI6'])))
	RSI12.append(str(float(row['RSI12'])))
	three_openposition.append(float(row['three_openposition']))
	openposition.append(float(row['openposition']))
	SMA5.append(str(float(row['SMA5'])))
	SMA10.append(str(float(row['SMA10'])))
	Volume.append(str(float(row['Volume'])))
	MA5.append(str(float(row['MA5'])))
	MA10.append(str(float(row['MA10'])))
	DIF12.append(str(float(row['DIF12'])))
	MACD9.append(str(float(row['MACD9'])))
	OSC.append(str(float(row['OSC'])))
	K.append(str(float(row['K'])))
	D.append(str(float(row['D'])))
	AR10.append(str(float(row['AR10'])))
	RSV5.append(str(float(row['RSV5'])))
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))
	price_high.append(float(row['High']))
	price_low.append(float(row['Low']))
dowfile2.close()


#file = open('../../../output/45/test-data','w')
file = open('./test-data','w')


for day in range(5,len(Open),1):

	if price_close[day]>price_open[day]:
		a='1'
	elif price_close[day]<=price_open[day]:
		a='-1'
	else :
		a='0'
	file.write(a)

	number = 0

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Open[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Close[i])
	'''
	for i in range(day-1,day-3,-1):
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

	for i in range(day-1,day-3,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Di2add[i])

	for i in range(day-1,day-3,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Di2minus[i])

	for i in range(day-1,day-3,-1):
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

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSI6[i])

	for i in range(day-1,day-6,-1):
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

	for i in range(day-1,day-3,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+str(three_openposition[i]))

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(three_openposition[i]>0):
			label=1
		else:
			label=-1
		file.write(' '+b+':'+str(label))

	for i in range(day-1,day-3,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+str(openposition[i]))

	for i in range(day-1,day-2,-1):
		number+=1
		b = str(number)
		if(openposition[i])>0:
			label=1
		else:
			label=-1
		file.write(' '+b+':'+str(label))
	'''
	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA5[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA10[i])
	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Volume[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MA5[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MA10[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+DIF12[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MACD9[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+OSC[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+K[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+D[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+AR10[i])

	for i in range(day-1,day-6,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSV5[i])

	file.write('\n')
file.close()