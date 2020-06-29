'''
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 

限制：

0 <= 数组长度 <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        max_v = 0
        min_v = prices[0]
        for i in range(1,len(prices)):
            max_v = max(prices[i]-min_v,max_v)
            min_v = min(min_v,prices[i])
        return  max_v

        #单次买入股票 动态规划
        # 设动态规划列表 dpdp ，dp[i]dp[i] 代表以 prices[i]prices[i] 为结尾的子数组的最大利润
        # dp[i]=max(dp[i−1],prices[i]−min(prices[0:i]))
        # dp = [0] * len(prices)
        # min_v = prices[0]
        # for i in range(1, len(prices)):
        #     dp[i] = max(dp[i-1], prices[i]-min_v)
        #     min_v = min(min_v, prices[i])
        # return max(dp)