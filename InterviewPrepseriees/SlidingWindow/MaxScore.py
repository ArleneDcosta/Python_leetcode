from typing import List


def maxScore(cardPoints: List[int], k: int) -> int:
    if k == len(cardPoints):
        return sum(cardPoints)
    
    resArr = []
    
    for i in range(0,k):
        if i == 0:
            resArr.append(sum(cardPoints[0:k]))
            resArr.append(sum(cardPoints[-k:]))
        else:
            resArr.append(sum(cardPoints[0:i] + cardPoints[-(k-i):]))

    return max(resArr)

def maxScoreOp(cardPoints: List[int], k: int) -> int:
    n = len(cardPoints)
    
    # Take the first k elements as initial sum
    current_sum = sum(cardPoints[:k])
    max_sum = current_sum
    
    # Slide the window: remove from front, add from back
    for i in range(1, k + 1):
        print(k - i, -i)
        current_sum = current_sum - cardPoints[k - i] + cardPoints[-i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

if __name__ == '__main__':
    # cardPoints = [9,7,7,9,7,7,9]
    # k = 7
    # print(maxScore(cardPoints,k))

    # cardPoints = [1,2,3,4,5,6,1]
    # k = 3
    # print(maxScore(cardPoints,k))

    # cardPoints = [1,79,80,1,1,1,200,1]
    # k = 3
    # print(maxScore(cardPoints,k))

    cardPoints = [100,40,17,9,73,75]
    k = 3
    print(maxScoreOp(cardPoints,k))