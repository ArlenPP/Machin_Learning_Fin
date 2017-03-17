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
v_SMA5 = []

dowfile = open('./train.csv','r')

for row in csv.DictReader(dowfile):
	Open.str(append(float(row['Open'])))
	Close.str(append(float(row['Close'])))
	Volume.str(append(float(row['Volume'])))
	High.str(append(float(row['High'])))
	Low.str(append(float(row['Low'])))
	SMA5.str(append(float(row['SMA5'])))
	SMA10.str(append(float(row['SMA10'])))
	SMA20.str(append(float(row['SMA20'])))
	SMA60.str(append(float(row['SMA60'])))
	MA5.str(append(float(row['MA5'])))
	MA10.str(append(float(row['MA10'])))
	DIF.str(append(float(row['DIF'])))
	ACD9.str(append(float(row['ACD9'])))
	OSC.str(append(float(row['OSC'])))
	K.str(append(float(row['K'])))
	D.str(append(float(row['D'])))
	RSI6.str(append(float(row['RSI6'])))
	RSI12.str(append(float(row['RSI12'])))
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))
	v_SMA5.append(float(row['SMA5']))
dowfile.close()


file = open('../output/4/train-data','w')


for day in range(0,len(Open)-2,1):	
		
	
	if price_close[day+1]>price_open[day+1]:
		a='1'
	elif price_close[day+1]<=price_open[day+1]:
		a='-1'

	R1 = str((v_SMA5[day+1]-v_SMA5[day])/2)
	
	file.write(a+' 1:'+RSI6[day]+' 2:'+RSI12[day]+' 3:'+SMA5[day]+' 4:'+SMA10[day]+' 5:'+SMA20[day])
	file.write(' 6:'+SMA60[day]+' 7:'+DIF[day]+' 8:'+ACD9[day]+' 9:'+OSC[day]+' 10:'+K[day]+' 11:'+D[day])
	file.write(' 12:'+Open[day]+' 13:'+Close[day])
	file.write(' 14:'+Volume[day]+' 15:'+MA5[day]+' 16:'+MA10[day])
	file.write(' 17:'+High[day]+' 18:'+Low[day]+' 19:'+R1)
	file.write('\n')


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
v_SMA5 = []

dowfile2 = open('./test.csv','r')

for row in csv.DictReader(dowfile2):
	Open.str(append(float(row['Open'])))
	Close.str(append(float(row['Close'])))
	Volume.str(append(float(row['Volume'])))
	High.str(append(float(row['High'])))
	Low.str(append(float(row['Low'])))
	SMA5.str(append(float(row['SMA5'])))
	SMA10.str(append(float(row['SMA10'])))
	SMA20.str(append(float(row['SMA20'])))
	SMA60.str(append(float(row['SMA60'])))
	MA5.str(append(float(row['MA5'])))
	MA10.str(append(float(row['MA10'])))
	DIF.str(append(float(row['DIF'])))
	ACD9.str(append(float(row['ACD9'])))
	OSC.str(append(float(row['OSC'])))
	K.str(append(float(row['K'])))
	D.str(append(float(row['D'])))
	RSI6.str(append(float(row['RSI6'])))
	RSI12.str(append(float(row['RSI12'])))
	price_open.append(float(row['Open']))
	price_close.append(float(row['Close']))
	v_SMA5.append(float(row['SMA5']))
dowfile2.close()

file2 = open('../output/4/test-data','w')


for day in range(0,len(Open)-2,1):	
		
	
	if price_close[day+1]>price_open[day+1]:
		a='1'
	elif price_close[day+1]<=price_open[day+1]:
		a='-1'

	R1 = str((v_SMA5[day+1]-v_SMA5[day])/2)


	file2.write(a+' 1:'+RSI6[day]+' 2:'+RSI12[day]+' 3:'+SMA5[day]+' 4:'+SMA10[day]+' 5:'+SMA20[day])
	file2.write(' 6:'+SMA60[day]+' 7:'+DIF[day]+' 8:'+ACD9[day]+' 9:'+OSC[day]+' 10:'+K[day]+' 11:'+D[day])
	file2.write(' 12:'+Open[day]+' 13:'+Close[day])
	file2.write(' 14:'+Volume[day]+' 15:'+MA5[day]+' 16:'+MA10[day])
	file2.write(' 17:'+High[day]+' 18:'+Low[day]+' 19:'+R1)
	file2.write('\n')