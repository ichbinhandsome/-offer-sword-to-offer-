'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
'''
class Solution:
    def numWays(self, n: int) -> int:
        #动态规划 斐波那契数列变形
        if n == 0:
            return 1
        if n <= 2:
            return n
        dp = [0 for i in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]%(1000000007)

        # if n == 0:
        #         return 1
        # if n <= 2:
        #     return n
        # a, b = 1, 2 
        # for i in range(2,n):
        #     a , b = b%(1000000007) , (a+b)%(1000000007)
        # return b