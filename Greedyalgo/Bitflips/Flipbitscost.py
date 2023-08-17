#same as minNumerKconsecutiveFlips except k is full string[not predefined all characters after curr string]
#Only diff is i+k < n : that is an additional req in the minNumberK problem
def flipbits(l):
    cost = 0
    for b in l:
        if cost % 2 == 0: b = b
        else: b = not b

        if b % 2 == 1: continue
        else: cost +=1

    return cost

#Other testcase, here k is by default
if __name__ == '__main__':
    print(flipbits([0,1,0,1]))
    print(flipbits([1,1,0]))