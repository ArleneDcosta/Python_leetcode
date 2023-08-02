
import sys

# Function to count number of steps
# required to reach a destination
    
# source -> source vertex
# step -> value of last step taken
# dest -> destination vertex
def steps(source, step, dest):
    print source,step,dest
    if (abs(source) > (dest)):
        return sys.maxsize 
    
    if (source == dest):
        return step

    pos = steps(source + step + 1,step + 1, dest)
    neg = steps(source - step - 1, step + 1, dest)
    print source,pos,neg,'pos','neg'
    return min(pos, neg)
    

# Driver Code
dest = 3
print("No. of steps required"," to reach " ,dest , " is " , steps(0, 0, dest));
    

# This code is contributed by Sam007.
