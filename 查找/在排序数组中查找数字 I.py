'''
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
 

限制：

0 <= 数组长度 <= 50000

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #第一种方法 哈希表
        # res = Counter(nums)
        # return res[target] if target in res else 0

        #第二种
        #普通二分查找 查找到目标后向左向右拓展
        # count  = 0
        # left, right = 0, len(nums)-1
        # while left <= right:
        #     mid = (left+right)//2
        #     if nums[mid] == target:
        #         count += 1
        #         p = mid-1
        #         q = mid+1
        #         while p >= left and nums[p] == target:
        #             count += 1
        #             p -= 1
        #         while q <= right and nums[q] == target:
        #             count += 1
        #             q += 1
        #         return count
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return 0

        #第三种
        #二分查找 找右边界
        #寻找target的右边界，寻找target-1的右边界， 两者相减即为所得
        # def binary_search(target):
        #     left, right = 0, len(nums)
        #     while left < right:
        #         mid = (left + right)//2
        #         if nums[mid] > target:
        #             right = mid
        #         elif nums[mid] <= target:
        #             left = mid + 1
        #     return left
        # return binary_search(target)-binary_search(target-1)

        #第四种
        #迭代 先找右边界 再找左边界 两者之差-1
        if not nums: return 0
        left,right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] > target: right = mid-1
            else: left = mid + 1
        #提前剪枝 没有找到该元素
        if left-1 >=0  and nums[left-1] != target: return 0
        l = left
        #只需对left重新赋值
        left = 0
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target: left = mid+1
            else: right = mid-1
        r = right
        return l-r-1
        