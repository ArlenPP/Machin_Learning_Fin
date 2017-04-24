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
Openposition = []
ChangeOpenposition = []
price_close= []
price_open = []
price_high = []
price_low = []

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
	Openposition.append(str(float(row['Openposition'])))
	ChangeOpenposition.append(str(float(row['ChangeOpenposition'])))
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))
	price_high.append(float(row['High']))
	price_low.append(float(row['Low']))
dowfile.close()


file = open('../../../output/43/train-data','w')
#file = open('./train-data','w')

for day in range(20,len(Open)-30,1):

	if price_close[day]>(price_open[day]):
		a='1'
	elif (price_close[day])<price_open[day]:
		a='-1'
	else :
		a='0'
	file.write(a)

	number = 0
	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Open[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Close[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA5[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA10[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA20[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+SMA60[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MA5[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+MA10[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+DIF[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+ACD9[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+OSC[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+K[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+D[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSI6[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+RSI12[i])

	for i in range(day-1,day-3,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+Openposition[i])

	for i in range(day-1,day-3,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+ChangeOpenposition[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+str(price_close[i]-price_open[i]))

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+str(price_high[i]-price_open[i]))

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file.write(' '+b+':'+str(price_low[i]-price_open[i]))

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
Openposition = []
ChangeOpenposition = []
price_close= []
price_open = []
price_high = []
price_low = []

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
	Openposition.append(str(float(row['Openposition'])))
	ChangeOpenposition.append(str(float(row['ChangeOpenposition'])))
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))
	price_high.append(float(row['High']))
	price_low.append(float(row['Low']))
dowfile2.close()

file2 = open('../../../output/43/test-data','w')
#file2 = open('./test-data','w')



for day in range(20,len(Open)-30,1):

	if price_close[day+30]>(price_open[day]):
		a='1'
	elif (price_close[day+30])<price_open[day]:
		a='-1'
	else :
		a='0'
	file2.write(a)

	number = 0
	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+Open[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+Close[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+SMA5[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+SMA10[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+SMA20[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+SMA60[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+MA5[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+MA10[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+DIF[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+ACD9[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+OSC[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+K[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+D[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+RSI6[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+RSI12[i])

	for i in range(day-1,day-3,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+Openposition[i])

	for i in range(day-1,day-3,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+ChangeOpenposition[i])

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+str(price_close[i]-price_open[i]))

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+str(price_high[i]-price_open[i]))

	for i in range(day-1,day-21,-1):
		number+=1
		b = str(number)
		file2.write(' '+b+':'+str(price_low[i]-price_open[i]))


	file2.write('\n')
file2.close()

