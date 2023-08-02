def word(w):
    w.sort(key=len)
    print w
    for word in w[::-1]:
        found =  True
        for i in range(1,len(word)):
            prefix = word[:i]
            print prefix
            if prefix not in w:
                found = False
                break
        if found:
            return word
    return ""


print word(["a", "banana", "app", "appl", "ap", "apply", "apple"])
