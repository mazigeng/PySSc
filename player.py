
EVEN = 0
ODD = 1

from wallet import *
from seller import *


class player(object):
    def __init__(self):
    	self.multiple = 1
    	self.chess = [EVEN]
    	self.stack = []
    	self.wallet = wallet()
        self.counter = Seller()
        self.curCost = 0
        pass

    def SetResult(self,judge, number,cost):
        self.stack.append(int(number[-1]))
        if len(self.stack) > 10:
            self.stack.pop(0)

        self.chess = self.MaxOccur(self.stack)
        self.wallet.ChangeM(cost[1] - cost[0])
        self.Multiple(judge, 0.4)

        pass

    def Choice(self):
        self.curCost += self.counter.Cost(self.multiple)
     	return (self.chess, self.multiple)
        pass

    def Resume(self):
        self.wallet.SaveMoney()
        self.multiple = 1
        self.curCost = 0

    def MaxOccur(self,List):
        ret = None
        listNum = List[:]
        listNum.sort()
        i = 0
        maxCnt = 10
        while(i < len(listNum)):
            cnt = listNum.count(listNum[i])
            if maxCnt > cnt:
                maxCnt = cnt
                ret = [listNum[i]]
            i += cnt
        return ret

    def Multiple(self, result, pre):
        if result :
            self.multiple = 1.0
            self.curCost = 0
        else:
            while self.counter.Pay(self.multiple) - self.counter.Cost(self.multiple) - self.curCost <= pre *self.multiple:
                self.multiple += 1

        if self.wallet.money - self.counter.Cost(self.multiple) < 0:
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

