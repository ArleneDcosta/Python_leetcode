
# Assume its sorted
class Solution:
    def __init__(self):
        self.dates = []
        self.company = {}
        self.baseamount = 1000.0

    def add_trade(self,l):

        for i in range(0,len(l),3):
            #self.inputlist.append(l[i:i+3])
            self.dates.append(l[i+1])

            if l[i] not in self.company:
                self.company[l[i]] = [[l[i+1],float(l[i+2])]]
            else:
                if float(l[i + 2]) < self.company[l[i]][0][1]:
                    self.company[l[i]].pop(0)
                self.company[l[i]] += [[l[i + 1], float(l[i + 2])]]
        self.dates = list(set(self.dates))

    def compute_profit(self,buyprice,sellprice,basevalue):
        return float(basevalue / buyprice) * float(sellprice)


    def run(self):
        #print(self.inputlist)

        minval = {}
        profdiff = {}
        #
        for key in sorted(self.dates):
            for ele in self.company.keys():
                if self.company[ele] and self.company[ele][0][0] == key:

                    if ele not in minval:
                        minval[ele] = self.company[ele][0][1]
                        profdiff[ele] = [0,self.baseamount]
                    else:
                        # Calculate profit
                        if (self.company[ele][0][1] - minval[ele]) > profdiff[ele][0]:
                            basevalue = profdiff[ele][1]
                            oldprofit = self.compute_profit(minval[ele],self.company[ele][0][1],basevalue)

                            if oldprofit > basevalue  :
                                profdiff[ele] = [self.company[ele][0][1] - minval[ele],oldprofit]
                                self.baseamount = oldprofit
                        if self.company[ele][0][1] < minval[ele]:
                            minval[ele] = self.company[ele][0][1]
                            profdiff[ele] = [profdiff[ele][0], self.baseamount]
                    self.company[ele].pop(0)
                else:
                    continue


        resprofit  = 0
        for company in profdiff:
            if profdiff[company][1] - 1000 > resprofit:
                resprofit = profdiff[company][1] - 1000

        return round(resprofit)




if __name__ == '__main__':
    l = ['IBM','12/01/2023','132.05','IBM','12/03/2023','135.19','IBM','12/18/2023','134.07',
         'AAPL','12/01/2023','187.19','AAPL','12/04/2023','164.33','AAPL','12/20/2023','180.94','AAPL','12/21/2023','179.65',
         'GOOG','12/01/2023','116.41','GOOG','12/07/2023','111.36','GOOG','12/19/2023','112.19']

    l1 = ['CSCO','10/18/2024','41.89','AMZN','10/10/2024','113.67','AMZN','10/18/2024','120.5','CSCO','10/10/2024','43.12']
    obj =  Solution()
    # First example test
    obj.add_trade(l1)
    print(obj.run())
    obj1 = Solution()
    # Second example test
    obj1.add_trade(l)
    print(obj1.run())