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


##====    set up config 	====##

train_data_startday = '2002/1/2'
train_data_endday = '2011/12/30'
test_data_startday = '2012/1/2'
test_data_endday = '2012/12/28'

over_x_is_high = 100
over_y_is_low =  100
transation_Time = 1
train_data_feature_few_day = 10
on_arlen_computer = 0
file = '53'
##====		set up where is history option file 		====##
dir_of_stock = './tmp_database/'


##==== set up file dir 		====##
if(on_arlen_computer == 1):
	train = open('./train-data','w')
	test = open('./test-data','w')
else:
	train = open('../../../output/'+file+'/train-data','w')
	test = open('../../../output/'+file+'/test-data','w')


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
number = []
number.append(int(1))
for i in range(0,(my_stock_combination.stock_list[0].TrainEndi - my_stock_combination.stock_list[0].TrainStarti)+1,1):
	number[0] = 1
	for my_stock in my_stock_combination.stock_list:
		
		if(my_stock.stockname == '1txff.csv'):
			HighOrLowHappened = 0
			for x in range(transation_Time):
				if(my_stock.High[my_stock.TrainStarti+i+x] > my_stock.Open[my_stock.TrainStarti+i]+over_x_is_high):
					train.write('1')
					HighOrLowHappened = 1
					break
				elif(my_stock.Low[my_stock.TrainStarti+i+x] < my_stock.Open[my_stock.TrainStarti+i]-over_y_is_low):
					train.write('-1')
					HighOrLowHappened = 1
					break
			if(HighOrLowHappened == 0):
				train.write('0')
		
		##==== con if is train == 1 if is test == 0 	====##
		con = 1
		FeatureWrite(train,train_data_feature_few_day,my_stock,i,number,con)
	train.write('\n')

##		make test 		##

for i in range(0,(my_stock_combination.stock_list[0].TestEndi - my_stock_combination.stock_list[0].TestStarti)+1,1):
	number[0] = 1
	for my_stock in my_stock_combination.stock_list:
		
		if(my_stock.stockname == '1txff.csv'):
			HighOrLowHappened = 0
			for x in range(transation_Time):
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
		##==== con if is train == 1 if is test == 0 	====##
		con = 0
		FeatureWrite(test,train_data_feature_few_day,my_stock,i,number,con)
	test.write('\n')