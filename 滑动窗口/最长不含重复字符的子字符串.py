'''
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

提示：

s.length <= 40000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #brute force O(n^2)
        # n = len(s)
        # res = 0
        # for i in range(n):
        #     hash_table = {}
        #     j = i
        #     while j < n and s[j] not in hash_table:
        #         hash_table[s[j]] = 1
        #         j += 1
        #     res  =  max(res, j-i)
        # return res

        #sliding-window + hash_table
        hash_table = {} #存储遍历过的元素以及它最后一次出现时的索引
        #siding window start-point: i   end-point:j
        i, j = 0, 0   #每次都需要去确定i的位置， 而j从零开始一直到结束遍历
        res = 0
        for j in range(len(s)):
            #当出现重复元素时，更新i
            if s[j] in hash_table:
                #这里为什么要max，是怕i倒退。因为如果只让i = hash_table[s[j]] + 1 有可能会忽略
                #之前已经更新过的i，从而忽略之前遍历过出现的重复元素，只专注与当前元素，不可取
                i = max(i, hash_table[s[j]] + 1)
             #存储或更新当前元素索引
            hash_table[s[j]] = j
            #更新res j-i+1: 当前有效window的长度
            res = max(j- i + 1, res)
        return res