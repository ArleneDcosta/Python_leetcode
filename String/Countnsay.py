def countnsay(n):
    if n==1:
        return "1"
    base="1"
    for i in range(2,n+1):
        new_base,temp="",[]
        a,c=base[0],0
        print('a:',a,'c:',c,'base:',base)
        for j in base: 
            if j==a: c += 1
            else:
                temp.append([str(c),a])
                a,c=j,1
        temp.append([str(c),a])
        print temp,i
        for k in temp: new_base += k[0]+k[1]
        base=new_base
    return base
#how would u say one digit below eg: count(3) one two one one 
#for 4 it would be count(5) one 1 one 2 and 2 ones
print countnsay(5)
