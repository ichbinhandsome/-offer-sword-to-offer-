'''
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

 

示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8
 

限制：

1 <= 数组长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # 同时找左右两边，left 为第一个值大于索引的数的索引， 所以结果为left
        # right 是最后一个索引等于值的元素的索引

        # left, right = 0, len(nums)-1
        # while left <= right:
        #     mid = (left+right)//2
        #     if nums[mid] == mid: left = mid + 1
        #     else: right = mid -1
        # return left



        #右边第一位nums[mid] != mid 的数
        if len(nums) == 1: return 0 if nums[0]==1 else 1
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right)//2
            if nums[mid-1] == mid-1 and nums[mid] != mid: return mid
            elif nums[mid] == mid: left = mid + 1
            else: right = mid
        return left #right
       