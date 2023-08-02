def div(dividend, divisor):
    """Assumes quotient is in-bounds, and divisor and dividend are both negative."""
    quotient = 0
    #As for positive converted both nums to negative
    #-7 < = -3
    print(dividend,divisor)
    while dividend <= divisor:
        #power +=1
        power = 0
        #-6
        while divisor << (power + 1) > dividend:
            
            power += 1
        dividend -= divisor << power
        #-7 -(-6) = -1
        #dividend = -1
        print(dividend)
       print(power)
        quotient += 1 << power
        #quotient = 2
    #-1 > -3 
    return quotient
        
def divide(dividend, divisor) :
    # Handle out-of bounds result 
    if dividend == -2**31 and divisor == -1:
        return 2**31 - 1
        
    # Convert both numbers to negative, remembering if the signs were different
    negative = False
    if dividend > 0 and divisor > 0:
        dividend = -dividend
        divisor = -divisor
    elif dividend > 0:
        dividend = -dividend
        negative = True
    elif divisor > 0:
        divisor = -divisor
        negative = True
     
    if negative:
        return -div(dividend, divisor)
    else:
        return div(dividend, divisor)
print divide(-7,3)
