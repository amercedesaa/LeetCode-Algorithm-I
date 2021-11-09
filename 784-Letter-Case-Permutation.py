class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        perm = ['']
        for l in s:
            if l.isalpha():
                perm = [x + y for x in perm for y in [l.lower(), l.upper()]]
            else:
                perm = [x + l for x in perm]
        return perm
