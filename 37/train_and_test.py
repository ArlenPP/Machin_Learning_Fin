import os
import csv


Open = []
High = []
Low = []
Close = []
EMA5 = []
EMA10 =[]
RSV9 = []
DIF = []
MACD5 = []
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
    High.append(str(float(row['High'])))
    Low.append(str(float(row['Low'])))
    EMA5.append(str(float(row['EMA5'])))
    EMA10.append(str(float(row['EMA10'])))
    RSV9.append(str(float(row['RSV9'])))
    DIF.append(str(float(row['DIF'])))
    MACD5.append(str(float(row['MACD5'])))
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


file = open('../../../output/37/train-data','w')

for day in range(5,len(Open),1):

    if price_close[day]>(price_open[day]+40):
        a='1'
    elif (price_close[day]+40)<price_open[day]:
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

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file.write(' '+b+':'+EMA5[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file.write(' '+b+':'+EMA10[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file.write(' '+b+':'+RSV9[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file.write(' '+b+':'+DIF[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file.write(' '+b+':'+MACD5[i])

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
        file.write(' '+b+':'+RSI6[i])

    for i in range(day-1,day-6,-1):
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

    for i in range(day-1,day-4,-1):
        number+=1
        b = str(number)
        file.write(' '+b+':'+str(price_close[i]-price_open[i]))

    for i in range(day-1,day-4,-1):
        number+=1
        b = str(number)
        file.write(' '+b+':'+str(price_high[i]-price_open[i]))

    for i in range(day-1,day-4,-1):
        number+=1
        b = str(number)
        file.write(' '+b+':'+str(price_low[i]-price_open[i]))

    file.write('\n')
file.close()




Open = []
High = []
Low = []
Close = []
EMA5 = []
EMA10 =[]
RSV9 = []
DIF = []
MACD5 = []
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
    High.append(str(float(row['High'])))
    Low.append(str(float(row['Low'])))
    EMA5.append(str(float(row['EMA5'])))
    EMA10.append(str(float(row['EMA10'])))
    RSV9.append(str(float(row['RSV9'])))
    DIF.append(str(float(row['DIF'])))
    MACD5.append(str(float(row['MACD5'])))
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

file2 = open('../../../output/37/test-data','w')



for day in range(5,len(Open),1):

    if price_close[day]>(price_open[day]+40):
        a='1'
    elif (price_close[day]+40)<price_open[day]:
        a='-1'
    else :
        a='0'
    
    file2.write(a)

    number = 0
    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+Open[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+Close[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+EMA5[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+EMA10[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+RSV9[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+DIF[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+MACD5[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+OSC[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+K[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+D[i])

    for i in range(day-1,day-6,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+RSI6[i])

    for i in range(day-1,day-6,-1):
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

    for i in range(day-1,day-4,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+str(price_close[i]-price_open[i]))

    for i in range(day-1,day-4,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+str(price_high[i]-price_open[i]))

    for i in range(day-1,day-4,-1):
        number+=1
        b = str(number)
        file2.write(' '+b+':'+str(price_low[i]-price_open[i]))

    file2.write('\n')


    file2.write('\n')
file2.close()

