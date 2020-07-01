'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        i, j = 0, len(nums)-1
        
        #中间元素将数组分为左右两部分，无论数组怎么旋转，左右两部分必有一方是有序的
        # 当 nums[mid] > nums[right] 时， 左侧元素是有序的
        # 当nums[mid] < nums[right] 时， 右侧元素是有序的

        while i <= j :
            mid = (i+j)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[j]: # 右侧有序
                if  nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid -1
            else: # 左侧有序
                if nums[i]<= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
        return -1