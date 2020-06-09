'''
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chou-shu-lcof
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # ugly_nums = [1] #额外数组存储丑数
        # max_ugly = ugly_nums[-1]
        # i, j, k = 0, 0 , 0
        # # 空间换时间
        # while len(ugly_nums) < n:
        #     max_ugly = ugly_nums[-1] # 目前丑数中最大的一个
        #     while ugly_nums[i] * 2 <= max_ugly:
        #         i += 1 #记录丑数*2 大于 max 的索引
        #     while ugly_nums[j] * 3 <= max_ugly:
        #         j += 1 #记录丑数*3 大于 max 的索引
        #     while ugly_nums[k] * 5 <= max_ugly:
        #         k += 1 #记录丑数*5 大于 max 的索引
        #     #选择这三个丑数中最小的一个，即为下一个丑数， 目的是保持丑数数组的单调递增
        #     next_ugly = min(ugly_nums[i] * 2, ugly_nums[j] * 3, ugly_nums[k] * 5)
        #     ugly_nums.append(next_ugly)
        # return ugly_nums[-1]

        #动态规划 思路与上述相似，判别条件和状态转移方程不一致
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]

