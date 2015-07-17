
from pprint import *

class DataMgr(object):
	def __init__(self):
		self.datas = []
		pass

	def SetDataFile(self,path):
		''' Set a data.txt file as data source.
		''' 
		f = open(path)
		strDatas = f.read()
		temp = []
		for one in strDatas.split('\n'):
			for piece in one.split('\t'):
				result = None
				if len(piece) > 12:
					result = ''.join(piece[3:12].split(' '))

				temp.append((piece[:3],result))
			if len(temp) == 120:
				temp.sort()
				self.datas += temp
				temp = []

	def GetData(self):
		for one in self.datas:
			yield one


	def GetValue(self):
		for one in self.datas:
			yield one[1]

	def GetNumber(self):
		for one in self.datas:
			yield one[0]



if __name__ == '__main__':
	d = DataMgr()
	d.SetDataFile('datas.txt')

	for one in d.GetData():
		print one
		raw_input()
