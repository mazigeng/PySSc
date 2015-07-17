


class Rule(object):
	def __init__(self):
		pass

	def RunOnce(self,data,choice):
		result = None
		if not(data[1] is None) and not(choice[0] is None):
			if int(data[1][-1]) in choice[0]:
				result = True
			else:
				result = False

		return result




if __name__ == '__main__':

	pass



