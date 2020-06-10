'''
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        # dp = [nums[0]] * len(nums)
        # # dp[i] 代表以元素 nums[i]nums[i] 为结尾的连续子数组最大和
        # for i in range(1,len(nums)):
        #     dp[i] = max(nums[i], nums[i]+dp[i-1])
        # return max(dp)

        #节省空间复杂度的动态规划，在原数组上进行操作
        # for i in range(1,len(nums)):
        #     nums[i] += max(0, nums[i-1])
        # return max(nums)
        
        #贪心
        res = nums[0]
        curr_sum = nums[0]
        for i in range(1,len(nums)):
            print(curr_sum)
            if curr_sum + nums[i] < nums[i]:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            res = max(curr_sum, res)
        return res
         

