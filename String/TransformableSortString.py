from collections import deque
'''Maintain relative distance of other subarrays'''
'''Check: If you have a number smaller than the current number then move the element to the first place '''
def isTransformable(s: str, t: str) -> bool:
    n = len(s)
    #popleft to remove the appr index
    indexes = [deque() for _ in range(10)]

    for i,c in enumerate(s):
        indexes[int(c)].append(i)

    for t_c in t:
        t_num = int(t_c)
        #If not present in source
        if not indexes[t_num]:
            return False
        for smaller_num in range(t_num):
            print(t_num,smaller_num)
            # means you are trying to swap/sort a number that is aldready sorted
            if indexes[smaller_num] and indexes[smaller_num][0] < indexes[t_num][0]:
                return False

        indexes[t_num].popleft()
    return True


if __name__ == '__main__':
    #print(isTransformable(s = "84532", t = "34852"))
    print(isTransformable(s = "12345", t = "12435"))