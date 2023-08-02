def isValid( s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        mapping = {')':'(','}':'{',']':'['}
               
        for x in s:
            
            if x in mapping:
                
                if stack and stack[-1] == mapping[x]:
                    stack.pop()
                else:
                    # this covers the case that the string starts with a closing bracket
                    return False
            else:
                stack.append(x)
            
        if stack:
            return False
        else:
            return True
