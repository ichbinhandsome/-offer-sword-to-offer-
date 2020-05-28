class Solution:
    def replaceSpace(self, s: str) -> str:
        if not s:
            return s
        re = ['%20' if i == ' ' else i for i in s]
        return ''.join(re)
