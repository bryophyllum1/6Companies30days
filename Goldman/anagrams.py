class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            temp = list(strs[i])
            temp.sort()
            x = "".join(temp)
            if x in d:
                d[x].append(strs[i])
            else:
                d[x] = [strs[i]]
        ans = []
        for key in d:
            ans.append(d[key])
        return ans