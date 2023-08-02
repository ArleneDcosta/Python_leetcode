def check(s):
    result = []
    for word in s:
        if word.isdigit()==False:
            result.append(word)
    result.sort()
    final = ''.join(result)
    print final
check('5edcab')
