'''
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
 

提示：

2 <= n <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof
'''
class Solution:
    def cuttingRope(self, n: int) -> int:
        #两种不同的思路

        # if n <= 2: return 1
        # if n == 3: return 2
        # dp  = [0] * (n+1)
        #不需要考虑剪或者不剪，因为初始化已经找出来剪或者不剪的最大值，只需要递推即可
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 2 #不剪2时最大值为2
        # dp[3] = 3 #不剪3时最大值为3
        # for i in range(4,n+1):
        #     for j in range(i//2+1):
        #         dp[i] = max(dp[i], dp[j] * dp[i-j])
        # return dp[-1] % (1000000007)
        
        #考虑最后一步的情况，向前推导
        dp = [0] * (n+1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n+1):
            for j in range(1, i):
                # dp[i] = max(dp[i], dp[i-j]*j, (i-j)*j)
                #每次考虑两种情况，剪或者不剪
                dp[i] = max(dp[i], (i-j)*dp[j], (i-j)*j)
        return dp[-1]% (1000000007)