'''
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = "" 
返回 " "

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
'''
class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return ' '
        hash_table ={}
        for i in s:
            if i not in hash_table:
                hash_table[i] = 1
            else:
                hash_table[i] += 1
        for i in s:
            if hash_table[i] == 1:
                return i
        return ' '
