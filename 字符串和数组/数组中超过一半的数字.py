'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 

限制：

1 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 
        # return sorted(nums)[len(nums)//2] #排序法
        # 摩尔投票法： 核心理念为 “正负抵消” ；时间和空间复杂度分别为 O(N)O(N) 和 O(1)O(1)
        votes = 0
        for num in nums:
            if votes == 0: mode = num
            if num == mode: votes += 1
            else: votes -= 1
        return mode