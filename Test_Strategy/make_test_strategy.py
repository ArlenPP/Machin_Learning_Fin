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

test_data_startday = '2016/1/4'
test_data_endday = '2016/12/30'

##====		set up where is history option file 		====##
dir_of_stock = './test_tmp_database/'

##==== set up file dir 		====##
test = open('./test-data','w')