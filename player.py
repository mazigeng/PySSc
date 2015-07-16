
EVEN = 0
ODD = 1

from wallet import *
from seller import *


class player(object):
    def __init__(self):
    	self.multiple = 1
    	self.chess = EVEN
    	self.stack = []
    	self.wallet = wallet()
    	self.cnt = 0
        self.conter = Seller()
        pass

    def SetResult(self,judge, number):
    	if judge :
    		self.multiple = 1.0
    	else:
    		self.multiple *= 3
    		if self.multiple > 1000:
    			self.multiple = 1.0
    		self.stack.append( int(number[-1]) % 2)
    		if len(self.stack) == self.cnt:
    			self.ChangeCnt()
    			self.chess = (self.chess + 1) % 2
    			self.stack = []


        pass

    def Choice(self):
     	return (self.chess, self.multiple)
        pass

    def ChangeCnt(self):
    	if self.cnt % 2 :
    		self.cnt = 1
    	else:
    		self.cnt = 2

    def Resume(self):
        self.wallet.SaveMoney()
        self.chess = EVEN
        self.stack = []
        self.multiple = 1
        self.cnt = 0


class player2(player):
    def __init__(self):
        super(player2,self).__init__()
        self.chess = 0
        self.cnt = 0
        self.stack = []
        self.cost = 0

    def SetResult(self,judge,number):
        self.stack.append(int(number[-1]))
        if len(self.stack) > 15:
            self.stack.pop(0)

        listNum = self.stack[:]
        listNum.sort()
        i = 0
        maxCnt = 0
        while(i < len(listNum)):
            cnt = listNum.count(listNum[i])
            if maxCnt < cnt:
                maxCnt = cnt
                self.chess = listNum[i]
            i += cnt



        if judge :
            self.multiple = 1.0
            self.cost = 0
        else:
            while self.multiple * 1.7 - self.cost <= 0.9*self.multiple:
                self.multiple += 1

        self.cost += self.multiple * 0.2

        if self.wallet.money - self.multiple * 0.2 < 0:
            self.Resume()





if __name__ == '__main__':

    p = player2()
    p.SetResult(False, "2")
    p.SetResult(False, "2")
    p.SetResult(False, "1")
    p.SetResult(True, "2")
    print p.Choice()


    '''
	p = player()
	p.SetResult(False, "2")
	p.SetResult(False, "2")
	p.SetResult(False, "1")
	p.SetResult(True, "2")
	print p.Choice()
    '''

