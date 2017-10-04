import os
import csv
import math
import datetime
import codecs
import re
from dateutil.relativedelta import relativedelta
from stock_class import stock
from stock_class import stock_combination
from stock_class import FeatureWrite
from stock_class import HighLowHappened



##====    set up config 	====##

train_data_startday = '2004/1/2'
train_data_endday = '2005/10/31'
test_data_startday = '2012/1/2'
test_data_endday = '2012/12/28'

over_x_is_high = 80
over_y_is_low =  80
stoplow = 12

##==== 0 is today,1 is today and tommorrow,etc ====##
transation_Time = 0
train_data_feature_few_day = 3
make_right_result = 0
on_arlen_computer = 1
file = '53'

control_call_times = 1
control_puttimes = 1
##====		set up where is history option file 		====##
dir_of_stock = '../tmp_database/'


##==== set up file dir 		====##
if(on_arlen_computer == 1):
	train = open('./train-data','w')
	test = open('./test-data','w')
else:
	train = open('../../../../output/'+file+'/train-data','w')
	test = open('../../../../output/'+file+'/test-data','w')

one_min_txff = csv.DictReader(open('../database/1min_txff_19980722_20150325_part1.csv','r'))
##====		START code 		====##
##====		read stock file 		====##

filelist_stock = [] #list of tmp_option.csv filename

for filename in os.listdir(dir_of_stock):
	filelist_stock.append(filename)

#====		good initial sort but doesnt sort numerically very well so we need to use key: and f:
def natural_key(string_):
	return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

filelist_stock.sort(key=natural_key)

##==== 		open stock file 	====##

my_stock_combination = stock_combination(filelist_stock)

##==== 		append data into my_stock 	====##
for my_stock in my_stock_combination.stock_list:
	tmp = open(dir_of_stock+my_stock.stockname,'r')
	my_stock.AppendData(tmp)

##==== 		start to make train and test 	 ====##
for my_stock in my_stock_combination.stock_list:
	
	##==== 	Enter Train Test START and End Day ====##
	for i in range(len(my_stock.Open)):
		if(my_stock.Date[i] == train_data_startday):
			my_stock.TrainStarti = i
		if(my_stock.Date[i] == train_data_endday):
			my_stock.TrainEndi = i
		if(my_stock.Date[i] == test_data_startday):
			my_stock.TestStarti = i
		if(my_stock.Date[i] == test_data_endday):
			my_stock.TestEndi = i
	print (my_stock.TrainStarti,my_stock.TestEndi)
	print my_stock.stockname
##====		make train 		====##
## range(i_of_startday,i_of_endday,+=1 each time)
#number = []
#number.append(int(1))

train_label_list = []
test_label_list = []


#==== creat raw label list ====#
for stock_data in my_stock_combination.stock_list:
	if(stock_data.stockname == 'txff.csv'):
		for i in range(0,(stock_data.TrainEndi - stock_data.TrainStarti)+1,1):
			label = HighLowHappened(stock_data.Open[stock_data.TrainStarti+i],stock_data.High[stock_data.TrainStarti+i],stock_data.Low[stock_data.TrainStarti+i],over_x_is_high,over_y_is_low)
			if(label == 1):
				train_label_list.append(1)
			elif(label == -1):
				train_label_list.append(-1)
			elif(label == 0):
				train_label_list.append(0)
			elif(label == 2):
				train_label_list.append(2)
				
		for i in range(0,(stock_data.TestEndi - stock_data.TestStarti)+1,1):
			label = HighLowHappened(stock_data.Open[stock_data.TestStarti+i],stock_data.High[stock_data.TestStarti+i],stock_data.Low[stock_data.TestStarti+i],over_x_is_high,over_y_is_low)
			if(label == 1):
				test_label_list.append(1)
			elif(label == -1):
				test_label_list.append(-1)
			elif(label == 0):
				test_label_list.append(0)
			elif(label == 2):
				test_label_list.append(2)

#==== modify labels by one mins ====#
onemin_Date = []
onemin_Open = []
onemin_High = []
onemin_Low = []

control_x = 0

for row in one_min_txff:
	onemin_Date.append(row['Date'])
	onemin_Open.append(float(row['Open']))
	onemin_High.append(float(row['High']))
	onemin_Low.append(float(row['Low']))

onemine_endTrain = 0
onemine_endTest = 0

for number in range(len(onemin_Date)):
	if(onemin_Date[number] == train_data_endday):
		onemine_endTrain = number + 301
		print (onemine_endTrain)
		break

for number in range(len(onemin_Date)):
	if(onemin_Date[number] == test_data_endday):
		onemine_endTest = number + 301
		print (onemine_endTest)
		break
		
#==== make train_label ====#
for i in range(len(train_label_list)):
	checkornot = 0
	if(train_label_list[i] == 1):
		for stock_data in my_stock_combination.stock_list:
			if(stock_data.stockname == 'txff.csv'):
				for x in range(control_x,onemine_endTrain,1):
					if((datetime.datetime.strptime(stock_data.Date[stock_data.TrainStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x], '%Y/%m/%d')) and checkornot == 0):
						print (onemin_Date[x])
						print (train_label_list[i])
						control_x = x
						for y in range(301):
							if(datetime.datetime.strptime(stock_data.Date[stock_data.TrainStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x+y], '%Y/%m/%d')):
								TodayOpen = stock_data.Open[stock_data.TrainStarti + i]
								ThisMinHigh = onemin_High[x+y]
								ThisMinLow = onemin_Low[x+y]
								if(TodayOpen - stoplow > ThisMinLow and checkornot == 0):
									train_label_list[i] = 0
									print (train_label_list[i])
									checkornot = 1
								elif(TodayOpen + over_x_is_high < ThisMinHigh and checkornot == 0):
									checkornot = 1

	elif(train_label_list[i] == -1):
		for stock_data in my_stock_combination.stock_list:
			if(stock_data.stockname == 'txff.csv'):
				for x in range(control_x,onemine_endTrain,1):
					if((datetime.datetime.strptime(stock_data.Date[stock_data.TrainStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x], '%Y/%m/%d')) and checkornot == 0):
						print (onemin_Date[x])
						control_x = x
						for y in range(301):
							if(datetime.datetime.strptime(stock_data.Date[stock_data.TrainStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x+y], '%Y/%m/%d')):
								TodayOpen = stock_data.Open[stock_data.TrainStarti + i]
								ThisMinHigh = onemin_High[x+y]
								ThisMinLow = onemin_Low[x+y]
								if(TodayOpen + stoplow < ThisMinHigh and checkornot == 0):
									train_label_list[i] = 0
									checkornot = 1
								elif(TodayOpen - over_y_is_low > ThisMinLow and checkornot == 0):
									checkornot = 1
	elif(train_label_list[i] == 2):
		for stock_data in my_stock_combination.stock_list:
			if(stock_data.stockname == 'txff.csv'):
				for x in range(control_x,onemine_endTrain,1):
					if((datetime.datetime.strptime(stock_data.Date[stock_data.TrainStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x], '%Y/%m/%d')) and checkornot == 0):
						print (onemin_Date[x])
						control_x = x
						for y in range(301):
							if(datetime.datetime.strptime(stock_data.Date[stock_data.TrainStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x+y], '%Y/%m/%d')):
								TodayOpen = stock_data.Open[stock_data.TrainStarti + i]
								ThisMinHigh = onemin_High[x+y]
								ThisMinLow = onemin_Low[x+y]
								if(TodayOpen + over_x_is_high > ThisMinHigh and checkornot == 0):
									train_label_list[i] = 1
									checkornot = 1
									for z in range(301):
										checkornot2 = 0
										if(datetime.datetime.strptime(stock_data.Date[stock_data.TrainStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x-y+z], '%Y/%m/%d')):
											TodayOpen = stock_data.Open[stock_data.TrainStarti + i]
											ThisMinHigh = onemin_High[x-y+z]
											ThisMinLow = onemin_Low[x-y+z]
											if(TodayOpen + over_x_is_high < ThisMinHigh and checkornot2 == 0):
												checkornot2 = 1
											elif(TodayOpen - stoplow > ThisMinLow and checkornot2 == 0):
												train_label_list[i] = 0
												checkornot2 = 1

								elif(TodayOpen - over_y_is_low > ThisMinLow and checkornot == 0):
									train_label_list[i] = -1
									checkornot = 1
									for z in range(301):
										checkornot2 = 0
										if(datetime.datetime.strptime(stock_data.Date[stock_data.TrainStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x-y+z], '%Y/%m/%d')):
											TodayOpen = stock_data.Open[stock_data.TrainStarti + i]
											ThisMinHigh = onemin_High[x-y+z]
											ThisMinLow = onemin_Low[x-y+z]
											if(TodayOpen + stoplow < ThisMinHigh and checkornot2 == 0):
												train_label_list[i] = 0
												checkornot2 = 1
											elif(TodayOpen - over_y_is_low > ThisMinLow and checkornot2 == 0):
												checkornot2 = 1

#==== make test label ====#


for i in range(len(test_label_list)):
	checkornot = 0
	if(test_label_list[i] == 1):
		for stock_data in my_stock_combination.stock_list:
			if(stock_data.stockname == 'txff.csv'):
				for x in range(control_x,onemine_endTest,1):
					if((datetime.datetime.strptime(stock_data.Date[stock_data.TestStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x], '%Y/%m/%d')) and checkornot == 0):
						print (onemin_Date[x])
						print (test_label_list[i])
						control_x = x
						for y in range(301):
							if(datetime.datetime.strptime(stock_data.Date[stock_data.TestStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x+y], '%Y/%m/%d')):
								TodayOpen = stock_data.Open[stock_data.TestStarti + i]
								ThisMinHigh = onemin_High[x+y]
								ThisMinLow = onemin_Low[x+y]
								if(TodayOpen - stoplow > ThisMinLow and checkornot == 0):
									test_label_list[i] = 0
									print (test_label_list[i])
									checkornot = 1
								elif(TodayOpen + over_x_is_high < ThisMinHigh and checkornot == 0):
									checkornot = 1

	elif(test_label_list[i] == -1):
		for stock_data in my_stock_combination.stock_list:
			if(stock_data.stockname == 'txff.csv'):
				for x in range(control_x,onemine_endTest,1):
					if((datetime.datetime.strptime(stock_data.Date[stock_data.TestStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x], '%Y/%m/%d')) and checkornot == 0):
						print (onemin_Date[x])
						control_x = x
						for y in range(301):
							if(datetime.datetime.strptime(stock_data.Date[stock_data.TestStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x+y], '%Y/%m/%d')):
								TodayOpen = stock_data.Open[stock_data.TestStarti + i]
								ThisMinHigh = onemin_High[x+y]
								ThisMinLow = onemin_Low[x+y]
								if(TodayOpen + stoplow < ThisMinHigh and checkornot == 0):
									test_label_list[i] = 0
									checkornot = 1
								elif(TodayOpen - over_y_is_low > ThisMinLow and checkornot == 0):
									checkornot = 1
	elif(test_label_list[i] == 2):
		for stock_data in my_stock_combination.stock_list:
			if(stock_data.stockname == 'txff.csv'):
				for x in range(control_x,onemine_endTest,1):
					if((datetime.datetime.strptime(stock_data.Date[stock_data.TestStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x], '%Y/%m/%d')) and checkornot == 0):
						print (onemin_Date[x])
						control_x = x
						for y in range(301):
							if(datetime.datetime.strptime(stock_data.Date[stock_data.TestStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x+y], '%Y/%m/%d')):
								TodayOpen = stock_data.Open[stock_data.TestStarti + i]
								ThisMinHigh = onemin_High[x+y]
								ThisMinLow = onemin_Low[x+y]
								if(TodayOpen + over_x_is_high > ThisMinHigh and checkornot == 0):
									test_label_list[i] = 1
									checkornot = 1
									for z in range(301):
										checkornot2 = 0
										if(datetime.datetime.strptime(stock_data.Date[stock_data.TestStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x-y+z], '%Y/%m/%d')):
											TodayOpen = stock_data.Open[stock_data.TestStarti + i]
											ThisMinHigh = onemin_High[x-y+z]
											ThisMinLow = onemin_Low[x-y+z]
											if(TodayOpen + over_x_is_high < ThisMinHigh and checkornot2 == 0):
												checkornot2 = 1
											elif(TodayOpen - stoplow > ThisMinLow and checkornot2 == 0):
												test_label_list[i] = 0
												checkornot2 = 1

								elif(TodayOpen - over_y_is_low > ThisMinLow and checkornot == 0):
									test_label_list[i] = -1
									checkornot = 1
									for z in range(301):
										checkornot2 = 0
										if(datetime.datetime.strptime(stock_data.Date[stock_data.TestStarti + i], '%Y/%m/%d') == datetime.datetime.strptime(onemin_Date[x-y+z], '%Y/%m/%d')):
											TodayOpen = stock_data.Open[stock_data.TestStarti + i]
											ThisMinHigh = onemin_High[x-y+z]
											ThisMinLow = onemin_Low[x-y+z]
											if(TodayOpen + stoplow < ThisMinHigh and checkornot2 == 0):
												test_label_list[i] = 0
												checkornot2 = 1
											elif(TodayOpen - over_y_is_low > ThisMinLow and checkornot2 == 0):
												checkornot2 = 1

total = 0
calltimes = 0
puttimes = 0
nonetime = 0

for i in range(len(train_label_list)):
	if(train_label_list[i] == 1):
		calltimes += 1
	elif(train_label_list[i] == -1):
		puttimes += 1
	elif(train_label_list[i] == 0):
		nonetime += 1
	total += 1

number = []
number.append(int(1))

for i in range(0,(my_stock_combination.stock_list[0].TrainEndi - my_stock_combination.stock_list[0].TrainStarti)+1,1):	
	##==== con if is train == 1 if is test == 0 	====##
	if(train_label_list[i] == 1):
		cct = control_call_times
		while cct>0:
			number[0] = 1
			train.write(str(train_label_list[i]))
			for my_stock in my_stock_combination.stock_list:
				con = 1
				FeatureWrite(train,train_data_feature_few_day,my_stock,i,number,con)
			train.write('\n')
			cct -= 1
			
	elif(train_label_list[i] == -1):
		cp = control_puttimes
		while cp>0:
			number[0] = 1
			train.write(str(train_label_list[i]))
			for my_stock in my_stock_combination.stock_list:
				con = 1
				FeatureWrite(train,train_data_feature_few_day,my_stock,i,number,con)
			train.write('\n')
			cp -= 1
			
	else:
		number[0] = 1
		train.write(str(train_label_list[i]))
		for my_stock in my_stock_combination.stock_list:
			con = 1
			FeatureWrite(train,train_data_feature_few_day,my_stock,i,number,con)
		train.write('\n')
		

print (total, calltimes, puttimes,nonetime)
print ('control_call_times = '+str(float(2*nonetime/calltimes)))
print ('control_puttimes = '+str(float(2*nonetime/puttimes)))


##		make test 		##
if(make_right_result == 0):
	for i in range(0,(my_stock_combination.stock_list[0].TestEndi - my_stock_combination.stock_list[0].TestStarti)+1,1):
		number[0] = 1
		test.write(str(test_label_list[i]))
		for my_stock in my_stock_combination.stock_list:
			##==== con if is train == 1 if is test == 0 	====##
			con = 0
			FeatureWrite(test,train_data_feature_few_day,my_stock,i,number,con)
		test.write('\n')
'''  not modify yet don't use  by 10/3
elif(make_right_result == 1):
	test.write('labels\n')
	for i in range(0,(my_stock_combination.stock_list[0].TestEndi - my_stock_combination.stock_list[0].TestStarti)+1,1):
		number[0] = 1
		for my_stock in my_stock_combination.stock_list:
			
			if(my_stock.stockname == 'txff.csv'):
				HighOrLowHappened = 0
				for x in range(transation_Time+1):
					if(my_stock.High[my_stock.TestStarti+i+x] > my_stock.Open[my_stock.TestStarti+i]+over_x_is_high):
						test.write('1')
						HighOrLowHappened = 1
						break
					elif(my_stock.Low[my_stock.TestStarti+i+x] < my_stock.Open[my_stock.TestStarti+i]-over_y_is_low):
						test.write('-1')
						HighOrLowHappened = 1
						break
				if(HighOrLowHappened == 0):
					test.write('0')
		test.write('\n')
'''