import re
from cmath import isinf
def isNumber(s):
		# you can use s.split('e') only 
		# here split('e') is working for the exponate
    a = s.split('e')
    b = s.split('E')
    try:
			# when i split the e we get a 2 
			# it must a be a float if a have char other than 
        float(a[0])
        print(float(a[0]),a,b,len(a),len(b))
			#if a is not an int it will be false
			#here we have a[1] error which happen if there is 'E' not 'e' there we will go to   
        int(a[1])
			# if a is 2 and b is one this means there is e in a string
        return len(a) == 2 and len(b) == 1
    except:
        try:
            z = float(s)
            print("INSIDE EXCEPT")
            return not (isinf(z))
        except :
            try:
                print("INSDIE",b)			# The same as a but with 'E'
                float(b[0])
                int(b[1])
                return len(a) == 1 and len(b) == 2
            except:
					# if all of that is false return false
                return False 
l = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789","abc"]
#l = ["2e10","-90E3"]
for no in l:
    print(no,isNumber(no))
#l = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
#for no in l:
    #print(no,solve(no))
    
