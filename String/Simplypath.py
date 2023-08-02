import re
def simplifyPath(path):
    path = path.split('/') 
    stack = [] 
    for i in path:
        if i =='.' or i =='': # skip the . and //
            continue
        elif i == '..':  #if ".." is present we don't need anything before that so we pop all elements in the stack
            if stack: 
                stack.pop()
        else:
            stack.append(i)            
    return '/' + '/'.join(stack)

print(simplifyPath("/home/"))
print(simplifyPath("/../"))
print(simplifyPath("/home//foo/"))
