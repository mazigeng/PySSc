# -*- coding: utf-8 -*-
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
        self.num = 2
        self.cnt = 0
        self.errCnt = 0
        self.reMultiple = 1
        pass

    def SetResult(self,judge, number, cost):

        self.cnt += 1

        if self.cnt == 4:
            self.cnt = 0

            if self.chess[-1] % 2 :
                self.chess = [EVEN]
            else :
                self.chess = [ODD]

        self.Multiple(judge,0.1)
        self.wallet.ChangeM(cost[1] - cost[0])



    def SetResult3(self, judge, number, cost):
        self.chess = [int(number[-1])]
        self.Multiple(judge,0.1)
        if self.errCnt == 1:
            self.reMultiple = self.multiple
        self.wallet.ChangeM(cost[1] - cost[0])

        if judge :
            if self.errCnt >= 2:
                self.multiple = self.reMultiple
            self.errCnt = 0
        else:
            self.errCnt += 1


        if self.errCnt >=2:
            self.multiple = 0
            self.errCnt += 1

        


    def SetResult2(self,judge, number,cost):

        if judge or self.cnt >= 5:
            self.num += 1
            print self.num
            self.num %= 10
        self.chess = [self.num]
        self.cnt += 1

        
        

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
            pass
            #self.Resume()

    # 连续几次奖号，出现次数
    def Arithmetic(self, judge, number):
        self.stack.append(int(number[-1]))
        if len(self.stack) > 10:
            self.stack.pop(0)

        return self.MaxOccur(self.stack)




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

