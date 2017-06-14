import os
import csv

##====	set up config 		====##

over_x_is_high = 150
over_y_is_low =  150

class Stock:
	def __init__(self,id):
		self.stockid = id
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
		self.ACD9 = []
		self.OSC = []
		self.K = []
		self.D = []
		self.RSI6 = []
		self.RSI12 = []
		self.RSV9 = []
		self.price_close= []
		self.price_open = []
		self.price_high = []
		self.price_low = []

	def AppendData(self,openfile):
		for row in csv.DictReader(openfile):
			self.Open.append(str(float(row['Open'])))
			self.Close.append(str(float(row['Close'])))
			self.Volume.append(str(float(row['Volume'])))
			self.High.append(str(float(row['High'])))
			self.Low.append(str(float(row['Low'])))
			self.SMA5.append(str(float(row['SMA5'])))
			self.SMA10.append(str(float(row['SMA10'])))
			self.SMA20.append(str(float(row['SMA20'])))
			self.SMA60.append(str(float(row['SMA60'])))
			self.MA5.append(str(float(row['MA5'])))
			self.MA10.append(str(float(row['MA10'])))
			self.DIF.append(str(float(row['DIF'])))
			self.ACD9.append(str(float(row['ACD9'])))
			self.OSC.append(str(float(row['OSC'])))
			self.K.append(str(float(row['K'])))
			self.D.append(str(float(row['D'])))
			self.RSI6.append(str(float(row['RSI6'])))
			self.RSI12.append(str(float(row['RSI12'])))
			self.RSV9.append(str(float(row['RSV9'])))
			self.price_open.append(float(row['Open']))
			self.price_close.append(float(row['Close']))
			self.price_high.append(float(row['High']))
			self.price_low.append(float(row['low']))
	def OverHighHappened(self.today_open):
		pass
	def OverLowHappened(self.today_open):
		pass