


class Rule(object):
	def __init__(self):
		pass

	def RunOnce(self,data,choice):
		result = None
		if not(data[1] is None) and not(choice[0] is None):
			if choice[0][0] % 2 == int(data[1][-1]) % 2:
				result = True
			else :
				result = False

		return result
	def RunOnce2(self,data,choice):
		result = None
		if not(data[1] is None) and not(choice[0] is None):
			if str(choice[0][0]) in list(data[1])[-3:] :
				result = True
			else:
				result = False

		return result




if __name__ == '__main__':

	pass



