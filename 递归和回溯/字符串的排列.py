'''
输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
'''
class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s: return
        # self.res = set()
        self.res = []
        # DFS
        def dfs(strings,temp=''):
            if not strings: 
                self.res.append(temp)
                return
            seen = set()
            for i in range(len(strings)):
                if strings[i] not in seen:
                    seen.add(strings[i])
                    dfs(strings[:i]+strings[i+1:], temp+strings[i])
        dfs(s)
        return self.res

        #回溯法
        # def helper(start, end, strings):
        #     if start == end:
        #         # self.res.add(''.join(stings))
        #         self.res.append(''.join(strings))
        #         return
        #     dic = set() #为了剪枝
        #     for i in range(start, end+1):
        #         if strings[i] in dic: continue
        #         dic.add(strings[i])
                #交换回溯
        #         strings[i], strings[start] = strings[start], strings[i]
        #         helper(start+1,end, strings)
        #         strings[i], strings[start] = strings[start], strings[i]
        # s = list(s)
        # helper(0, len(s)-1, s)
        # # return list(self.res)
        # return self.res