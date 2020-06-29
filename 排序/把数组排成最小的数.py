'''
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

 

示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"
 

提示:

0 < nums.length <= 100
说明:

输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof
'''

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        # 本质上是排序问题 只不过排序规则发生了改变
        # 不是比较两数的大小， 而是比较两个字符串组合起来形成的数
        # eg. 给定字符串x,y 如果xy>yx，则证明x大于y，x需要放到y之后（升序数组）
        # x = '30', y = '6', '306' < '603', 则 x < y, x应该排在y之前

        nums = [str(i) for i in nums]
        n = len(nums)

        #简单冒泡排序
        # for i in range(n):
        #     for j in range(0, n-i-1):
        #         if int(nums[j] + nums[j+1]) > int(nums[j+1]+nums[j]):
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        # return ''.join(nums)

        #简单快速排序
        def quick_sort(start, end, nums):
            if start >= end: return
            standard = nums[start]
            i , j = start, end
            while i < j:
                while i < j and int(nums[j]+ standard) > int(standard+nums[j]): j -= 1
                nums[i] = nums[j]
                while i < j and int(nums[i] + standard) <= int(standard + nums[i]): i += 1
                nums[j] = nums[i]
            nums[i] = standard
            quick_sort(start, i-1, nums)
            quick_sort(i+1, end, nums)
        quick_sort(0, len(nums)-1, nums)
        return ''.join(nums)
