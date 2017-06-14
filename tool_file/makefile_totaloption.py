#!/usr/bin/python
# coding=utf8

import os
import csv
import math
import datetime
import codecs
import re
from dateutil.relativedelta import relativedelta

##====		set up where is history option file 		====##

dir_of_history_option = '../../History_Option/tmp_option/'

##====	read history option 請將檔案放在同一個資料夾裡面的folder which name is "option" ====##

dir_history_option = dir_of_history_option #directory of option.csv
filelist_history_option = [] #list of tmp_option.csv filename


for filename in os.listdir(dir_history_option):
	if('.csv' in filename):
		filelist_history_option.append(filename)
#====		good initial sort but doesnt sort numerically very well so we need to use key: and f:
def natural_key(string_):
	return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

filelist_history_option.sort(key=natural_key)

##====		create a totaloption csv file 		====##
totaloption = open('./totaloption.csv','w')
totaloption.write("date,dateline,type,strike_price,callorput,open,high,low,close,open_interest\n")

for filename in filelist_history_option:
	print(filename)

	tmp = codecs.open(dir_of_history_option+filename,'r','big5')
	optionfile = tmp.read()


	file = codecs.open('./tmpfile.csv','w','utf8')
	file.write(optionfile)


	for row in csv.DictReader(open('./tmpfile.csv')):
		if row['契約'] == 'TXO':
			if (row['買賣權']=='買權'):
				x='call'
			else:
				x='put'
			totaloption.write(row['交易日期']+','+row['到期月份(週別)']+','+row['契約']+','+row['履約價']+','+x+','+row['開盤價']+','+row['最高價']+','+row['最低價']+','+row['收盤價']+','+row['未沖銷契約數']+'\n')
totaloption.close()
