import os
import csv


Open = []
Close = []
Volume = []
High = []
Low = []
SMA5 = []
SMA10 =[]
SMA20 = []
SMA60 = []
MA5 = []
MA10 = []
DIF = []
ACD9 = []
OSC = []
K = []
D = []
RSI6 = []
RSI12 = []
RSV9 = []
price_close= []
price_open = []

Open1 = []
Close1 = []
Volume1 = []
High1 = []
Low1 = []
SMA51 = []
SMA101 =[]
SMA201 = []
SMA601 = []
MA51 = []
MA101 = []
DIF1 = []
ACD91 = []
OSC1 = []
K1 = []
D1 = []
RSI61 = []
RSI121 = []
RSV91 = []
price_close1= []
price_open1 = []

Open2 = []
Close2 = []
Volume2 = []
High2 = []
Low2 = []
SMA52 = []
SMA102 =[]
SMA202 = []
SMA602 = []
MA52 = []
MA102 = []
DIF2 = []
ACD92 = []
OSC2 = []
K2 = []
D2 = []
RSI62 = []
RSI122 = []
RSV92 = []
price_close2= []
price_open2 = []

dowfile = open('./train.csv','r')

for row in csv.DictReader(dowfile):
	Open.append(str(float(row['Open'])))
	Close.append(str(float(row['Close'])))
	Volume.append(str(float(row['Volume'])))
	High.append(str(float(row['High'])))
	Low.append(str(float(row['Low'])))
	SMA5.append(str(float(row['SMA5'])))
	SMA10.append(str(float(row['SMA10'])))
	SMA20.append(str(float(row['SMA20'])))
	SMA60.append(str(float(row['SMA60'])))
	MA5.append(str(float(row['MA5'])))
	MA10.append(str(float(row['MA10'])))
	DIF.append(str(float(row['DIF'])))
	ACD9.append(str(float(row['ACD9'])))
	OSC.append(str(float(row['OSC'])))
	K.append(str(float(row['K'])))
	D.append(str(float(row['D'])))
	RSI6.append(str(float(row['RSI6'])))
	RSI12.append(str(float(row['RSI12'])))
	RSV9.append(str(float(row['RSV9'])))
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))

	Open1.append(str(float(row['Open1'])))
	Close1.append(str(float(row['Close1'])))
	Volume1.append(str(float(row['Volume1'])))
	High1.append(str(float(row['High1'])))
	Low1.append(str(float(row['Low1'])))
	SMA51.append(str(float(row['SMA51'])))
	SMA101.append(str(float(row['SMA101'])))
	SMA201.append(str(float(row['SMA201'])))
	SMA601.append(str(float(row['SMA601'])))
	MA51.append(str(float(row['MA51'])))
	MA101.append(str(float(row['MA101'])))
	DIF1.append(str(float(row['DIF1'])))
	ACD91.append(str(float(row['ACD91'])))
	OSC1.append(str(float(row['OSC1'])))
	K1.append(str(float(row['K1'])))
	D1.append(str(float(row['D1'])))
	RSI61.append(str(float(row['RSI61'])))
	RSI121.append(str(float(row['RSI121'])))
	RSV91.append(str(float(row['RSV91'])))
	price_open1.append(float(row['Open1']))
	price_close1.append(float(row['Close1']))

	Open2.append(str(float(row['Open2'])))
	Close2.append(str(float(row['Close2'])))
	Volume2.append(str(float(row['Volume2'])))
	High2.append(str(float(row['High2'])))
	Low2.append(str(float(row['Low2'])))
	SMA52.append(str(float(row['SMA52'])))
	SMA102.append(str(float(row['SMA102'])))
	SMA202.append(str(float(row['SMA202'])))
	SMA602.append(str(float(row['SMA602'])))
	MA52.append(str(float(row['MA52'])))
	MA102.append(str(float(row['MA102'])))
	DIF2.append(str(float(row['DIF2'])))
	ACD92.append(str(float(row['ACD92'])))
	OSC2.append(str(float(row['OSC2'])))
	K2.append(str(float(row['K2'])))
	D2.append(str(float(row['D2'])))
	RSI62.append(str(float(row['RSI62'])))
	RSI122.append(str(float(row['RSI122'])))
	RSV92.append(str(float(row['RSV92'])))
	price_open2.append(float(row['Open2']))
	price_close2.append(float(row['Close2']))
dowfile.close()


file = open('../../../output/52/train-data','w')
#file = open('./train-data','w')

for day in range(10,len(Open),1):

	if price_close[day]>price_open[day]+100:
		a='1'
	elif price_close[day]+100<=price_open[day]:
		a='-1'
	else:
		a='0'
	if(a=='1' or a=='-1'):
		if(a=='1'):
			control = 24
		elif(a=='-1'):
			control = 20
		while control > 0:
			control -= 1
			file.write(a)
			number = 0
			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+Open[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+Close[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+SMA5[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+SMA10[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+SMA20[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+SMA60[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+MA5[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+MA10[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+DIF[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+ACD9[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+OSC[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+K[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+D[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+RSI6[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+RSI12[i])
			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+RSV9[i])

			#######

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+Open1[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+Close1[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+SMA51[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+SMA101[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+SMA201[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+SMA601[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+MA51[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+MA101[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+DIF1[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+ACD91[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+OSC1[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+K1[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+D1[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+RSI61[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+RSI121[i])
			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+RSV91[i])

				######

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+Open2[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+Close2[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+SMA52[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+SMA102[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+SMA202[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+SMA602[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+MA52[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+MA102[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+DIF2[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+ACD92[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+OSC2[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+K2[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+D2[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+RSI62[i])

			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+RSI122[i])
			for i in range(day-1,day-11,-1):
				number+=1
				b = str(number)
				file.write(' '+b+':'+RSV92[i])

			file.write('\n')



	else:
		file.write(a)
		number = 0
		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+Open[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+Close[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+SMA5[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+SMA10[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+SMA20[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+SMA60[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+MA5[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+MA10[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+DIF[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+ACD9[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+OSC[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+K[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+D[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+RSI6[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+RSI12[i])
		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+RSV9[i])

		#######

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+Open1[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+Close1[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+SMA51[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+SMA101[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+SMA201[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+SMA601[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+MA51[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+MA101[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+DIF1[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+ACD91[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+OSC1[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+K1[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+D1[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+RSI61[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+RSI121[i])
		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+RSV91[i])

			######

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+Open2[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+Close2[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+SMA52[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+SMA102[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+SMA202[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+SMA602[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+MA52[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+MA102[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+DIF2[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+ACD92[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+OSC2[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+K2[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+D2[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+RSI62[i])

		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+RSI122[i])
		for i in range(day-1,day-11,-1):
			number+=1
			b = str(number)
			file.write(' '+b+':'+RSV92[i])

		file.write('\n')

	
file.close()



Open = []
Close = []
Volume = []
High = []
Low = []
SMA5 = []
SMA10 =[]
SMA20 = []
SMA60 = []
MA5 = []
MA10 = []
DIF = []
ACD9 = []
OSC = []
K = []
D = []
RSI6 = []
RSI12 = []
RSV9 = []
price_close= []
price_open = []

Open1 = []
Close1 = []
Volume1 = []
High1 = []
Low1 = []
SMA51 = []
SMA101 =[]
SMA201 = []
SMA601 = []
MA51 = []
MA101 = []
DIF1 = []
ACD91 = []
OSC1 = []
K1 = []
D1 = []
RSI61 = []
RSI121 = []
RSV91 = []
price_close1= []
price_open1 = []

Open2 = []
Close2 = []
Volume2 = []
High2 = []
Low2 = []
SMA52 = []
SMA102 =[]
SMA202 = []
SMA602 = []
MA52 = []
MA102 = []
DIF2 = []
ACD92 = []
OSC2 = []
K2 = []
D2 = []
RSI62 = []
RSI122 = []
RSV92 = []
price_close2= []
price_open2 = []

dowfile2 = open('./test.csv','r')

for row in csv.DictReader(dowfile2):
	Open.append(str(float(row['Open'])))
	Close.append(str(float(row['Close'])))
	Volume.append(str(float(row['Volume'])))
	High.append(str(float(row['High'])))
	Low.append(str(float(row['Low'])))
	SMA5.append(str(float(row['SMA5'])))
	SMA10.append(str(float(row['SMA10'])))
	SMA20.append(str(float(row['SMA20'])))
	SMA60.append(str(float(row['SMA60'])))
	MA5.append(str(float(row['MA5'])))
	MA10.append(str(float(row['MA10'])))
	DIF.append(str(float(row['DIF'])))
	ACD9.append(str(float(row['ACD9'])))
	OSC.append(str(float(row['OSC'])))
	K.append(str(float(row['K'])))
	D.append(str(float(row['D'])))
	RSI6.append(str(float(row['RSI6'])))
	RSI12.append(str(float(row['RSI12'])))
	RSV9.append(str(float(row['RSV9'])))
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))

	Open1.append(str(float(row['Open1'])))
	Close1.append(str(float(row['Close1'])))
	Volume1.append(str(float(row['Volume1'])))
	High1.append(str(float(row['High1'])))
	Low1.append(str(float(row['Low1'])))
	SMA51.append(str(float(row['SMA51'])))
	SMA101.append(str(float(row['SMA101'])))
	SMA201.append(str(float(row['SMA201'])))
	SMA601.append(str(float(row['SMA601'])))
	MA51.append(str(float(row['MA51'])))
	MA101.append(str(float(row['MA101'])))
	DIF1.append(str(float(row['DIF1'])))
	ACD91.append(str(float(row['ACD91'])))
	OSC1.append(str(float(row['OSC1'])))
	K1.append(str(float(row['K1'])))
	D1.append(str(float(row['D1'])))
	RSI61.append(str(float(row['RSI61'])))
	RSI121.append(str(float(row['RSI121'])))
	RSV91.append(str(float(row['RSV91'])))
	price_open1.append(float(row['Open1']))
	price_close1.append(float(row['Close1']))

	Open2.append(str(float(row['Open2'])))
	Close2.append(str(float(row['Close2'])))
	Volume2.append(str(float(row['Volume2'])))
	High2.append(str(float(row['High2'])))
	Low2.append(str(float(row['Low2'])))
	SMA52.append(str(float(row['SMA52'])))
	SMA102.append(str(float(row['SMA102'])))
	SMA202.append(str(float(row['SMA202'])))
	SMA602.append(str(float(row['SMA602'])))
	MA52.append(str(float(row['MA52'])))
	MA102.append(str(float(row['MA102'])))
	DIF2.append(str(float(row['DIF2'])))
	ACD92.append(str(float(row['ACD92'])))
	OSC2.append(str(float(row['OSC2'])))
	K2.append(str(float(row['K2'])))
	D2.append(str(float(row['D2'])))
	RSI62.append(str(float(row['RSI62'])))
	RSI122.append(str(float(row['RSI122'])))
	RSV92.append(str(float(row['RSV92'])))
	price_open2.append(float(row['Open2']))
	price_close2.append(float(row['Close2']))
dowfile.close()

file = open('../../../output/52/test-data','w')
#file = open('./test-data','w')

for day in range(10,len(Open),1):

	if price_close[day]>price_open[day]+100:
		a='1'
	elif price_close[day]+100<=price_open[day]:
		a='-1'
	else:
		a='0'
	
	file.write(a)
	number = 0
	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Open[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Close[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA5[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA10[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA20[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA60[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MA5[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MA10[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+DIF[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+ACD9[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+OSC[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+K[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+D[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSI6[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSI12[i])
	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSV9[i])

	#######

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Open1[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Close1[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA51[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA101[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA201[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA601[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MA51[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MA101[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+DIF1[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+ACD91[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+OSC1[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+K1[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+D1[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSI61[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSI121[i])
	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSV91[i])

		######

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Open2[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Close2[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA52[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA102[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA202[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA602[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MA52[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MA102[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+DIF2[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+ACD92[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+OSC2[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+K2[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+D2[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSI62[i])

	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSI122[i])
	for i in range(day-1,day-11,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSV92[i])

	file.write('\n')

	
file.close()