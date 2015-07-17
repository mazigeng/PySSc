

class Seller(object):
	def __init__(self):
		self.pay = 1.7
		self.cost = 0.2
		pass

	def Count(self, result, multiple):
		ret = []
		if result is None:
			ret = [0,0]
		else:
			ret.append(self.Cost(multiple))
			if result :
				ret.append(self.Pay(multiple))
			else :
				ret.append(0)

		return ret

	def Cost(self,mul):
		return mul * self.cost

	def Pay(self,mul):
		return mul * self.pay


if __name__ == '__main__':
	s = Seller()
	print s.Count(False,1) #[0.2,0]
	print s.Count(True,1) #[0.2,1.7]
	print s.Count(None,1) #[0,0]
