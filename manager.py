

from Datas import *
from player import *
from rule import *
from seller import *

class Manager(object):
	def __init__(self):
		self.Datas = None
		self.itData = None
		self.Player = None

		pass

	def Init(self,path):
		self.InitDatas(path)
		self.InitPlayer()
		self.InitRule()
		self.InitSeller()

	def Run(self,day):
		for n in range(0,120*day):
			self.ShowRet(self.GameOnce())
		pass

	def GameOnce(self):
		ret = {}
		choice = self.Player.Choice()
		data = self.itData.next()
		result = self.Rule.RunOnce(data,choice)
		count = self.Seller.Count(result,choice[1])

		if not( result is None ):
			self.Player.SetResult(result,data[1],count)

		ret["time"] = data[0]
		ret["result"] = result
		ret["number"] = data[1]
		ret["choice"] = choice[0]
		ret["multiple"] = choice[1]
		ret["pay"] = count[1]
		ret["cost"] = count[0]
		ret["money"] = self.Player.wallet.money
		ret["sum"] = self.Player.wallet.SumMoney()

		return ret

	def ShowRet(self,dic):
		strShow = '%s\t%r\t%s\t%s\t%d\t%.1f\t-%.1f\t%.1f\t%.1f' % (dic["time"],dic["result"],dic["number"],dic["choice"],dic["multiple"],dic["pay"],dic["cost"],dic["money"],dic["sum"])
		print strShow


	def InitDatas(self,path):
		self.Datas = DataMgr()
		self.Datas.SetDataFile(path)
		self.itData = self.Datas.GetData()

	def InitPlayer(self):
		self.Player = player()

	def InitRule(self):
		self.Rule = Rule()

	def InitSeller(self):
		self.Seller = Seller()


if __name__ == '__main__':
	m = Manager()
	m.Init("datas.txt")
	for n in range(1,15) : 
		m.Run(1)
		raw_input()
