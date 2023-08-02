import json

d = [{'1':'1','viable':True},{'2':'2','viable':False}]


temp = json.dumps(d)
#temp1 = json.loads(temp)
testresult = [  1 for val in temp if val["viable"] == True]
print(testresult)

