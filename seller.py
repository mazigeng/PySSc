

class Seller(object):
	def __init__(self):
		self.pay = 1.7
		self.cost = 0.2
		pass

	def Cost(self,mul):
		return mul * self.cost

	def Pay(self,mul):
		return mul * self.pay