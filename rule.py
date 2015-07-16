


class Rule(object):
	def __init__(self):
		pass

	def RunOnce(self,data,choice):
		result = None
		if data[1] or choice[0]:
			if int(data[1][-1]) in choice[0]:
				result = True
			else:
				result = False

		return result




if __name__ == '__main__':
	from player import *
	from Datas import *

	p = player2()
	d = DataMgr()
	d.SetDataFile("datas.txt")

	r = Rule()
	r.SetPlayer(p)
	r.SetDatas(d)

	sum = 0

	for n in range(0,120*14):
		result = r.RunOnce()
		cost = 0.0
		pay = 0.0
		if result[2] :
			if result[1] :
				pay = 1.7 * result[4]
			cost = 0.2 * result[4]


			p.wallet.ChangeM(pay - cost)
			strShow = ''

			if result[2]:
				strShow = '%s\t%r\t%s\t%d\t%d\t%.1f\t-%.1f\t%.1f' % (result + (pay,cost,p.wallet.money))
			else :
				print 'sdfsdfsdf'
				strShow = '%s None' % result[0]
			print strShow
		if not ((n+1) % 120 ):
			p.wallet.SaveMoney()
			raw_input()
	print p.wallet.SumMoney()
	raw_input()



