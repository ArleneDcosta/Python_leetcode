def generateParenthesis(n):
    if n==1:
        return ["()"]
    else:
        x = generateParenthesis(n-1)
        result = []
        print x,n
        for i in x:
            temp = []
            for j in range(len(i)):
                temp.append(i[:j] + "()" + i[j:])
                print(i[:j] + "()" + i[j:])
            temp.append(i + "()")
            print temp,i+"()",i
            result.extend(temp)
        result = list(set(result))
        return result
print generateParenthesis(3)
