from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = []
    anagramDict = {}
    for string in strs:
        tempstring = "".join(sorted(string))
        if tempstring not in anagramDict:
            anagramDict[tempstring] = [string]
        else:
            anagramDict[tempstring].append(string)

    for key in anagramDict:
        res.append(anagramDict[key])
    return res

if __name__ == '__main__':
    print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
    print(groupAnagrams(strs = [""]))