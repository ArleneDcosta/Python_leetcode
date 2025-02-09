

def sumOfSubOdd(arr):
    mod, n = 10 ** 9 + 7, len(arr)
    odd_sum, even_sum, curr_sum, ans = 0, 1, 0, 0
    for i in arr:
        curr_sum += i
        if curr_sum % 2 == 1:
            odd_sum += 1
            ans += even_sum % mod
        else:
            even_sum += 1
            ans += odd_sum % mod
    ans %= mod


if __name__ == '__main__':
    arr = [1,3,5]
    print(sumOfSubOdd(arr))

    arr =  [1,2,3,4,5,6,7]
    print(sumOfSubOdd(arr))

    