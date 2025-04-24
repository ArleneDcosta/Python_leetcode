import bisect

def get_stock_span(arr):
    n = len(arr)
    span = [0] * n  
    stk = []
    for i in range(n):
        while stk and arr[stk[-1]] <= arr[i]:
            stk.pop()

        if not stk:
            span[i] = (i + 1)
        else:
            span[i] = (i - stk[-1])

        stk.append(i)

    return span
if __name__ == '__main__':
    arr = [100, 80, 60, 70, 60, 75, 85]
    print(get_stock_span(arr))

    arr = [10, 4, 5, 90, 120, 80]
    print(get_stock_span(arr))