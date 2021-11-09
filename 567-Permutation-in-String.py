class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=len(s1)
        l2=len(s2)
        l3=l2-l+1
        dic=Counter(s1)
        for i in range(l3):
            if Counter(s2[i:i+l])==dic:
                return True
        return False
