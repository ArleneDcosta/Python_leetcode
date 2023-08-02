def sumgame(num: str):
    # Alice will always try to maximise the difference and Bob will try to minimize the difference
    # when diff < 9: 43??, here Alice will put 9 because diff i.e 7 < 9
    # when diff > 9 : 7945:????, Alice will put 0 because she wants to max the diff and Bob will put 9 to min difference
    #  9 * cnt//2 = diff Bob wins or else Alice wins because Alice will put a 0 or 9
    n = len(num)
    cnt = diff = 0
    for i, c in enumerate(num):
        if i < n // 2:
            if c == '?':
                cnt += 1
            else:
                diff += int(c)
        else:
            if c == '?':
                cnt -= 1
            else:
                diff -= int(c)
    # case like 52??:0021 here Alice will put a zero and Bob will put a 9 so Alice wins
    if diff > 0 and cnt > 0:
        return True
    # case like 0041:52?? here Same values but on the opposite
    if diff < 0 and cnt < 0:
        return True

    # Remaining cases case 5299: 52?? and 9:?? Bob will always win 0:??
    print(cnt, diff)
    diff, cnt = abs(diff), abs(cnt)
    return cnt * 9 / 2 != diff


if __name__ == '__main__':
    print(sumgame('?3295???'))
