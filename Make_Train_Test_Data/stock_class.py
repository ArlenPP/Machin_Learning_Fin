import os
import csv


class stock_combination:
	stock_list = []
	def __init__(self,list):
		i = 0
		for stockname in list:
			self.stock_list.append(stock(i,str(stockname)))
			i += 1
		


class stock:
	def OverHighHappened(self,yesterday_open,):
		pass
	def OverLowHappened(self,today_open):
		pass
	def __init__(self,id,name):
		self.id = id
		self.stockname = name
		self.TrainStarti = 0
		self.TrainEndi = 0
		self.TestStarti = 0
		self.TestEndi = 0
		self.Date = []
		self.Open = []
		self.Close = []
		self.Volume = []
		self.High = []
		self.Low = []
		self.SMA5 = []
		self.SMA10 =[]
		self.SMA20 = []
		self.SMA60 = []
		self.MA5 = []
		self.MA10 = []
		self.DIF = []
		self.MACD9 = []
		self.OSC = []
		self.K = []
		self.D = []
		self.RSI6 = []
		self.RSI12 = []
		self.RSV9 = []
		self.RSV9_condition = []
		self.RSI6_RSI12_condition = []
		self.RSI6_tmp = []
		self.RSI_condition = []
		self.K_tmp = []
		self.K_D_condition =[]
		self.MACD9_tmp = []
		self.MACD9_DIF_condition = []
		
		self.Volume_MA5 = []
		self.Volume_MA10 = []
		self.Diff_Volume_MA5 = []
		self.Diff_Volume_MA10 = []
		## 	about SMA5 and SMA20 ##
		self.SMA_tmp = []
		self.SMA5_SMA20_condition = []
		## stock price and SMA ##
		self.Open_SMA5 = []
		self.Open_SMA10 = []
		self.Open_SMA20 = []
		self.Open_SMA60 = []

		self.High_SMA5 = []
		self.High_SMA10 = []
		self.High_SMA20 = []
		self.High_SMA60 = []

		self.Low_SMA5 = []
		self.Low_SMA10 = []
		self.Low_SMA20 = []
		self.Low_SMA60 = []

		self.Close_SMA5 = []
		self.Close_SMA10 = []
		self.Close_SMA20 = []
		self.Close_SMA60 = []

		## about price ##
		self.Diff_Open = []
		self.Diff_High = []
		self.Diff_Low = []
		self.Diff_Close = []
		self.Diff_Open_Close = []

		self.Diff_Open_SMA5 = []
		self.Diff_Open_SMA10 = []
		self.Diff_Open_SMA20 = []
		self.Diff_Open_SMA60 = []

		self.Diff_High_SMA5 = []
		self.Diff_High_SMA10 = []
		self.Diff_High_SMA20 = []
		self.Diff_High_SMA60 = []

		self.Diff_Low_SMA5 = []
		self.Diff_Low_SMA10 = []
		self.Diff_Low_SMA20 = []
		self.Diff_Low_SMA60 = []

		self.Diff_Close_SMA5 = []
		self.Diff_Close_SMA10 = []
		self.Diff_Close_SMA20 = []
		self.Diff_Close_SMA60 = []

	def AppendData(self,stock_file):
		for row in csv.DictReader(stock_file):
			self.Date.append(row['Date'])
			self.Open.append(float(row['Open']))
			self.Close.append(float(row['Close']))
			self.Volume.append(float(row['Volume']))
			self.High.append(float(row['High']))
			self.Low.append(float(row['Low']))
			self.SMA5.append(float(row['SMA5']))
			self.SMA10.append(float(row['SMA10']))
			self.SMA20.append(float(row['SMA20']))
			self.SMA60.append(float(row['SMA60']))
			self.MA5.append(float(row['MA5']))
			self.MA10.append(float(row['MA10']))
			self.DIF.append(float(row['DIF']))
			self.MACD9.append(float(row['MACD9']))
			self.OSC.append(float(row['OSC']))
			self.K.append(float(row['K']))
			self.D.append(float(row['D']))
			self.RSI6.append(float(row['RSI6']))
			self.RSI12.append(float(row['RSI12']))
			self.RSV9.append(float(row['RSV9']))
		for i in range(len(self.Open)):
			##==== about RSV9 ====##
			if(1 >= self.RSV9[i] >= 0.96):
				self.RSV9_condition.append(str(-1))
			elif(0.1 > self.RSV9[i]):
				self.RSV9_condition.append(str(1))
			else:
				self.RSV9_condition.append(str(0))
			
			##==== about RSI6 and RSI12 ====##
			if(self.RSI6[i] >= 0.79 and self.RSI12[i] >= 0.79):
				self.RSI6_RSI12_condition.append(str(-1))
			elif(0.2 > self.RSI6[i] and 0.2> self.RSI12[i]):
				self.RSI6_RSI12_condition.append(str(1))
			else:
				self.RSI6_RSI12_condition.append(str(0))
			
			##==== about RSI6 and RSI12 UP DOWN  	====##
			if(self.RSI6[i] > self.RSI12[i]):
				self.RSI6_tmp.append(float(1))
			else:
				self.RSI6_tmp.append(float(-1))
			if(i==0):
				self.RSI_condition.append(str(0))
			elif(self.RSI6_tmp[i]!=self.RSI6_tmp[i-1] and self.RSI6_tmp[i-1] == -1):
				self.RSI_condition.append(str(1))
			elif(self.RSI6_tmp[i]!=self.RSI6_tmp[i-1] and self.RSI6_tmp[i-1] == 1):
				self.RSI_condition.append(str(-1))
			else:
				self.RSI_condition.append(str(0))
			
			##==== about RSI6 and RSI12 UP DOWN  	====##
			if(self.K[i] > self.D[i]):
				self.K_tmp.append(float(1))
			else:
				self.K_tmp.append(float(-1))
			if(i==0):
				self.K_D_condition.append(str(0))
			elif(self.K_tmp[i] != self.K_tmp[i-1] and self.K_tmp[i-1] == 1):
				self.K_D_condition.append(str(1))
			elif(self.K_tmp[i] != self.K_tmp[i-1] and self.K_tmp[i-1] == -1):
				self.K_D_condition.append(str(-1))
			else:
				self.K_D_condition.append(str(0))
			##==== 	about MACD and DIF 		====##
			if(self.DIF[i] > self.MACD9[i]):
				self.MACD9_tmp.append(float(1))
			else:
				self.MACD9_tmp.append(float(-1))
			if(i==0):
				self.MACD9_DIF_condition.append(str(0))
			elif(self.MACD9_tmp[i] != self.MACD9_tmp[i-1] and self.MACD9_tmp[i-1] == 1):
				self.MACD9_DIF_condition.append(str(1))
			elif(self.MACD9_tmp[i] != self.MACD9_tmp[i-1] and self.MACD9_tmp[i-1] == -1):
				self.MACD9_DIF_condition.append(str(-1))
			else:
				self.MACD9_DIF_condition.append(str(0))
			##==== about normalize MA 		====##
			self.Volume_MA5.append(str(self.Volume[i]/self.MA5[i]))
			self.Volume_MA10.append(str(self.Volume[i]/self.MA10[i]))
			self.Diff_Volume_MA5.append(str((self.Volume[i]-self.MA5[i])/self.MA5[i]))
			self.Diff_Volume_MA10.append(str((self.Volume[i]-self.MA10[i])/self.MA10[i]))

			##==== about SMA5 and SMA20 ====##
			if(self.SMA5[i] > self.SMA20[i]):
				self.SMA_tmp.append(float(1))
			else:
				self.SMA_tmp.append(float(-1))
			if(i==0):
				self.SMA5_SMA20_condition.append(str(0))
			elif(self.SMA_tmp[i] != self.SMA_tmp[i-1] and self.SMA_tmp[i-1] == 1):
				self.SMA5_SMA20_condition.append(str(1))
			elif(self.SMA_tmp[i] != self.SMA_tmp[i-1] and self.SMA_tmp[i-1] == -1):
				self.SMA5_SMA20_condition.append(str(-1))
			else:
				self.SMA5_SMA20_condition.append(str(0))

			##==== about Stock Price 	====##
			self.Open_SMA5.append(str((self.Open[i]/self.SMA5[i])*100-100))
			self.Open_SMA10.append(str((self.Open[i]/self.SMA10[i])*100-100))
			self.Open_SMA20.append(str((self.Open[i]/self.SMA20[i])*100-100))
			self.Open_SMA60.append(str((self.Open[i]/self.SMA60[i])*100-100))

			self.High_SMA5.append(str((self.High[i]/self.SMA5[i])*100-100))
			self.High_SMA10.append(str((self.High[i]/self.SMA10[i])*100-100))
			self.High_SMA20.append(str((self.High[i]/self.SMA20[i])*100-100))
			self.High_SMA60.append(str((self.High[i]/self.SMA60[i])*100-100))

			self.Low_SMA5.append(str((self.Low[i]/self.SMA5[i])*100-100))
			self.Low_SMA10.append(str((self.Low[i]/self.SMA10[i])*100-100))
			self.Low_SMA20.append(str((self.Low[i]/self.SMA20[i])*100-100))
			self.Low_SMA60.append(str((self.Low[i]/self.SMA60[i])*100-100))

			self.Close_SMA5.append(str((self.Close[i]/self.SMA5[i])*100-100))
			self.Close_SMA10.append(str((self.Close[i]/self.SMA10[i])*100-100))
			self.Close_SMA20.append(str((self.Close[i]/self.SMA20[i])*100-100))
			self.Close_SMA60.append(str((self.Close[i]/self.SMA60[i])*100-100))
			##==== 	Diff price  ====##
			if(i==0):
				self.Diff_Open.append(str(0))
				self.Diff_High.append(str(0))
				self.Diff_Low.append(str(0))
				self.Diff_Close.append(str(0))
				self.Diff_Open_Close.append(str(0))
			else:
				self.Diff_Open.append(str(self.Open[i]-self.Open[i-1]))
				self.Diff_High.append(str(self.High[i]-self.High[i-1]))
				self.Diff_Low.append(str(self.Low[i]-self.Low[i-1]))
				self.Diff_Close.append(str(self.Close[i]-self.Close[i-1]))
				self.Diff_Open_Close.append(str(self.Open[i]-self.Close[i-1]))
			
			##==== 	Diff  open and SMA price  ====##		
			self.Diff_Open_SMA5.append(str(self.Open[i]-self.SMA5[i]))
			self.Diff_Open_SMA10.append(str(self.Open[i]-self.SMA10[i]))
			self.Diff_Open_SMA20.append(str(self.Open[i]-self.SMA20[i]))
			self.Diff_Open_SMA60.append(str(self.Open[i]-self.SMA60[i]))		
			##==== 	Diff  high and SMA price  ====##
			self.Diff_High_SMA5.append(str(self.High[i]-self.SMA5[i]))
			self.Diff_High_SMA10.append(str(self.High[i]-self.SMA10[i]))
			self.Diff_High_SMA20.append(str(self.High[i]-self.SMA20[i]))
			self.Diff_High_SMA60.append(str(self.High[i]-self.SMA60[i]))
			##==== 	Diff  low and SMA price  ====##
			self.Diff_Low_SMA5.append(str(self.Low[i]-self.SMA5[i]))
			self.Diff_Low_SMA10.append(str(self.Low[i]-self.SMA10[i]))
			self.Diff_Low_SMA20.append(str(self.Low[i]-self.SMA20[i]))
			self.Diff_Low_SMA60.append(str(self.Low[i]-self.SMA60[i]))
			##==== 	Diff  close and SMA price  ====##
			self.Diff_Close_SMA5.append(str(self.Close[i]-self.SMA5[i]))
			self.Diff_Close_SMA10.append(str(self.Close[i]-self.SMA10[i]))
			self.Diff_Close_SMA20.append(str(self.Close[i]-self.SMA20[i]))
			self.Diff_Close_SMA60.append(str(self.Close[i]-self.SMA60[i]))
			
def FeatureWrite(file,T,stock_in_my_stock_loop,i,number,c):
	if(c==1):
		dayi = stock_in_my_stock_loop.TrainStarti
	elif(c==0):
		dayi = stock_in_my_stock_loop.TestStarti

	for y in range(0,-T-1,-1):
		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.DIF[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.MACD9[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.OSC[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.K[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.D[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.RSI6[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.RSI12[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.RSV9[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.RSV9_condition[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.RSI6_RSI12_condition[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.RSI_condition[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.K_D_condition[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.MACD9_DIF_condition[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Volume_MA5[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Volume_MA10[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Volume_MA5[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Volume_MA10[dayi+i+y]))
		number[0] +=1

## 	about SMA5 and SMA20 ##

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.SMA5_SMA20_condition[dayi+i+y]))
		number[0] +=1

## stock price and SMA ##

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Open_SMA5[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Open_SMA10[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Open_SMA20[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Open_SMA60[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.High_SMA5[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.High_SMA10[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.High_SMA20[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.High_SMA60[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Low_SMA5[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Low_SMA10[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Low_SMA20[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Low_SMA60[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Close_SMA5[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Close_SMA10[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Close_SMA20[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Close_SMA60[dayi+i+y]))
		number[0] +=1


## about price ##
		
		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Open[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_High[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Low[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Close[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Open_Close[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Open_SMA5[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Open_SMA10[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Open_SMA20[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Open_SMA60[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_High_SMA5[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_High_SMA10[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_High_SMA20[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_High_SMA60[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Low_SMA5[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Low_SMA10[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Low_SMA20[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Low_SMA60[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Close_SMA5[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Close_SMA10[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Close_SMA20[dayi+i+y]))
		number[0] +=1

		file.write(' '+str(number[0])+':')
		file.write(str(stock_in_my_stock_loop.Diff_Close_SMA60[dayi+i+y]))
		number[0] +=1
