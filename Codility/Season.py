def solution(T):
    days=len(T)/4
    res=[]
    seasons = ['winter','spring','summer','autumn']
    
    for i in range(0,len(T),days):
        res.append(max(T[i:i+days])-min(T[i:i+days]))
        
    
    if days==1:
        res=T
    element=max(res)
    print res
    for i in range(0,4):
        if res[i]==element:
            return seasons[i]
def solution1(T):
        breaks = len(T)//4

        curr_max = T[0]
        curr_min = T[0]
        max_amp = 0
        max_amp_i = 0
        for i, temp in enumerate(T):
            print i,temp
            if i != 0 and i%breaks == 0:
                # season has ended
                curr_amp = abs(curr_max - curr_min)
                if curr_amp > max_amp:
                    max_amp = curr_amp
                    max_amp_i = (i-1)//breaks
                curr_max = temp
                curr_min = temp
            
            if temp < curr_min:
                curr_min = temp
            if temp > curr_max:
                curr_max = temp

        return {
            0:"WINTER",
            1:"SPRING",
            2:"SUMMER",
            3:"AUTUMN"
        }[max_amp_i]

print solution([-3,-14,-5,7,8,3,8,42])
print solution([-54,8,118,3])
print solution([-1,-54,-1,90,8,42,3,4,5,56,89,5])
print solution1([-3,-14,-5,7,8,3,8,42])
print solution1([-54,8,118,3])
print solution1([-1,-54,-1,90,42,5,3,4,65,56,89,5])
