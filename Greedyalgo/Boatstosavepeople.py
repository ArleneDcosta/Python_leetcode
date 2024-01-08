from typing import List

def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort(reverse=True)

    left = 0
    right = len(people) - 1
    print(people)
    ans  = 0
    while(left <= right):
        ans += 1
        if people[right] + people[left] <= limit:
            right -= 1

        left += 1

    return ans


if __name__ == '__main__':
    print(numRescueBoats(people = [3,2,2,1], limit = 3))
    print(numRescueBoats(people = [3,5,3,4], limit = 5))
    print(numRescueBoats(people = [1,2], limit = 3))
    print(numRescueBoats(people = [5,1,4,2],limit=6))
    print(numRescueBoats(people = [2,4],limit = 5))