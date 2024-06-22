def pushend(l):
    pos = 0
    for i in range(len(l)):
        if l[i] != 0:
            l[pos] = l[i]
            pos += 1
    for i in range(pos, len(l)):
        l[i] = 0

    return l

if __name__ == '__main__' :
    print(pushend([1, 2, 0, 4, -1, 5, 6, 0, 0, 7, 0]))
    print(pushend([0, 0, 2]))
