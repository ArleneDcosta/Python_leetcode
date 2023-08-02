
def soln():
    #Enter the variables
    i=int(x)
    #while for infinite loop
    while(True):
        print((x+","+int(x)*(y+",")),end="")
        print(i*(x+","+(int(y)*(y+","))),end="")
        i+=1
        
def inputfunc():
    x=str(input("Enter first positive integer")) 
    y=str(input("Enter second positive integer"))
    soln(x,y)


#testcases
soln(2,3)
soln(5,6)
