def grayCode(n):
    if n>=1:
        grayCode = [0, 1]
        for i in range(1, n):
            new = grayCode[::-1]
            print(f"new:{new}")
            for j in range(len(new)):
                print(i,j)
                new[j] += 2**(i)
            grayCode.extend(new)
            print(f"graycode:{grayCode}")
        return grayCode
    else:
        return [0]
        
print(grayCode(4))
