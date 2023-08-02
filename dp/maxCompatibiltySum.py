# if the constraint is 8 then the value would always be 2^8
from functools import lru_cache
# Greedy will make every student combine with different mentors it will be more complicated

def max_compatibility_sum(students,mentors):
    def getscore(s,m):
        ans = 0
        for i in range(n):
            if s[i] == m[i]:
                ans +=1
        return ans
    @lru_cache(None)

    def dp(i,mask):
        if i == m:
            # Each student has been assigned a mentor
            return 0
        # Try to assign all mentors to a student i
        ans = 0
        for j in range(m):
            if mask & ( 1<<j) == 0:
                ans =  max(ans ,getscore(students[i],mentors[j]) + dp(i+1, mask | (1<<j) ))

        return ans

    m = len(students)
    n = len(students[0]) #no of questions
    return dp(0,0)


if __name__ == '__main__':
    print(max_compatibility_sum([[1,1,0],[1,0,1],[0,0,1]],[[1,0,0],[0,0,1],[1,1,0]]))