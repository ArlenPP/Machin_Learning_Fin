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
price_close= []
price_open = []

dowfile = open('./train_random.csv','r')

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
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))
dowfile.close()


file = open('../../output/random/train-data','w')


for day in range(0,len(Open)-1,1):


	if price_close[day+1]>price_open[day+1]:
		a='1'
	elif price_close[day+1]<=price_open[day+1]:
		a='-1'

	file1.write(a+' 1:'+Open[day]+' 2:'+Close[day]+' 3:'+High[day]+' 4:'+Low[day]+' 5:'+Volume[day])

	#file.write(a+' 1:'+RSI6[day]+' 2:'+RSI12[day]+' 3:'+SMA5[day]+' 4:'+SMA10[day]+' 5:'+SMA20[day])
	#file.write(' 6:'+SMA60[day]+' 7:'+DIF[day]+' 8:'+ACD9[day]+' 9:'+OSC[day]+' 10:'+K[day]+' 11:'+D[day])
	#file.write(' 12:'+Open[day]+' 13:'+Close[day])
	#file.write(' 14:'+Volume[day]+' 15:'+MA5[day]+' 16:'+MA10[day])
	#file.write(' 17:'+High[day]+' 18:'+Low[day])
	#file.write('\n')


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
price_close= []
price_open = []

dowfile2 = open('./test_random.csv','r')

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
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))
dowfile2.close()

file2 = open('../../output/random/test-data','w')


for day in range(0,len(Open)-1,1):


	if price_close[day+1]>price_open[day+1]:
		a='1'
	elif price_close[day+1]<=price_open[day+1]:
		a='-1'

	file2.write(a+' 1:'+Open[day]+' 2:'+Close[day]+' 3:'+High[day]+' 4:'+Low[day]+' 5:'+Volume[day])

	#file2.write(a+' 1:'+RSI6[day]+' 2:'+RSI12[day]+' 3:'+SMA5[day]+' 4:'+SMA10[day]+' 5:'+SMA20[day])
	#file2.write(' 6:'+SMA60[day]+' 7:'+DIF[day]+' 8:'+ACD9[day]+' 9:'+OSC[day]+' 10:'+K[day]+' 11:'+D[day])
	#file2.write(' 12:'+Open[day]+' 13:'+Close[day])
	#file2.write(' 14:'+Volume[day]+' 15:'+MA5[day]+' 16:'+MA10[day])
	#file2.write(' 17:'+High[day]+' 18:'+Low[day])
	file2.write('\n')
