'''
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof
'''


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        # max_num = 10**n-1
        # return [i+1 for i in range(max_num)]
        self.res = []
        #全排列 回溯
        def dfs(n, temp):
            # if len(temp) == n:
            #     res.append(temp.copy())
            #     return 
            if len(temp) > n: return
            self.res.append(''.join(temp.copy()))
            for i in range(10):
                if (len(temp)==0 and i == 0): continue
                temp.append(str(i))
                dfs(n,temp)
                temp.pop()
        dfs(n,[])
        res = [int(i) for i in self.res if i]
        return sorted(res)

