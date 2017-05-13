import os
import csv
'''
def UporDown(today):
    for i in range(today+1,today+32,1):
        if(0.05<(price_high[i]-price_open[today])/price_open[today]):
            label = '1'
            print("in function label =1")
            break
        elif(0.05<(price_open[today]-price_low[i])/price_open[today]):
            label = '-1'
            print("in function label =-1")
            break
#[bug!!!] here has a bug because we only know price_high and price_low in a day
#but we don't know which one is the first one, so if price_low is the first then
#there will have a bug.
'''


def CsvDataToSVMdata(TXFI,mode):
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
    price_high = []
    price_low = []

    for row in csv.DictReader(TXFI):
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
        price_high.append(float(row['High']))
        price_low.append(float(row['Low']))


    if(mode=="train"):
        file = open('../../../output/51/train-data','w')
        #file = open('./train-data','w')
    elif(mode=="test"):
        file = open('../../../output/51/test-data','w')
        #file = open('./test-data','w')
    else:
        print("No~~~~~~~~~~~~~~~~")

    
    for day in range(10,len(Open)-30,1):
        label = '0'

        for x in range(day+1,day+31,1):
            if(0.05<(price_high[x]-price_open[day])/price_open[day]):
                label = '1'
                #print("in function label =1")
                break
            elif(0.05<(price_open[day]-price_low[x])/price_open[day]):
                label = '-1'
                #print("in function label =-1")
                break

        #UporDown(day)
        if(label=='1' or label=='-1'):
            if(label=='1'):
                control = 1
            elif(label=='-1'):
                control = 1
            while control > 0:
                control -= 1
                file.write(label)
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
                file.write('\n')

        else:
            file.write(label)
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
    
    file.write('\n')

train_TXFI = open('./train.csv','r')
CsvDataToSVMdata(train_TXFI,"train")
train_TXFI.close()

test_TXFI = open('./test.csv','r')
CsvDataToSVMdata(test_TXFI,"test")
test_TXFI.close()
