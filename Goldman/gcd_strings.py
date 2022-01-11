def check(s1, s2, c):
    i = 0
    j = 0
    while i+c<len(s1):
        if s1[i]!=s1[i+c]:
            return False
        i+=1
    while j+c<len(s2):
        if s2[j]!=s2[j+c]:
            return False
        j+=1
    return True
class Solution:
            
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        c = 0
        ans = 0
        for i in range(min(l1, l2)):
            if str1[i]==str2[i]:
                c+=1
                if l1%c==0 and l2%c==0 and check(str1, str2, c):
                    ans = c
        return str1[:ans]  