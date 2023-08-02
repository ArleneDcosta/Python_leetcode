def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        d = {}
        i=0
        for val in strs:
            s = "".join(sorted(val))
            if s not in d:
                d[s] =  i
                i+=1
        for c in range(0,i):
            result.append([])
        
        for val in strs:
            s = "".join(sorted(val))
            result[d[s]].append(val)
        return result

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
