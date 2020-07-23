'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
'''
class Solution:
    def isValid(self, s: str) -> bool:
        #使用栈
        # stack = []
        # hash_set ={'(':')', '[':']', '{':'}'}
        # for i in s:
        #     if i in hash_set:
        #         stack.append(i)
        #     else:
        #         if not stack:
        #             return False
        #         s = stack.pop()
        #         if hash_set[s] != i:
        #             return False
        # return not stack
        
        stack = []
        hash_set ={'(':')', '[':']', '{':'}'}
        for i in s:
            if not stack:
                stack.append(i)
            else:
                curr = stack[-1]
                if curr not in hash_set or hash_set[curr] != i:
                    stack.append(i)      
                elif hash_set[curr] == i:
                    stack.pop()     
        return not stack