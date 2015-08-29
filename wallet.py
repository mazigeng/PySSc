

InitMoney = 100.00

class wallet(object):
	def __init__(self):
		self.money = InitMoney
		self.bank = 0-InitMoney

	def ChangeM(self,m):
		self.money += m
		'''
		if self.money >= InitMoney*1.2:
			self.SaveMoney()
		'''

	def SaveMoney(self):
		self.bank += self.money - InitMoney
		self.money = InitMoney

	def SumMoney(self):
		return self.bank + self.money



