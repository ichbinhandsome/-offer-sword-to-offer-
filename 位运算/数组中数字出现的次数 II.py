'''
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

 

示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1
 

限制：

1 <= nums.length <= 10000
1 <= nums[i] < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #binary search
        # nums.sort()
        # left, right = 0 , len(nums)-1

        # while left <= right:
        #     mid = (left+right)//2

        #     #遇到结果提前剪枝（可以删除，提升代码简洁性）
        #     # if (mid-1 >= left and nums[mid] != nums[mid-1]) and (mid+1<=right and nums[mid] != nums[mid+1]):
        #     #     return nums[mid]

        #     l,r  = mid, mid
        #     #向左拓展判断数字是否相同
        #     while l-1 >= left and nums[l] == nums[l-1]: l -= 1
        #     #向右拓展数字是否相同
        #     while r + 1 <= right and nums[r] == nums[r+1]: r += 1
        #     #判断前面的数字个数能否被3整除，如果能被整除则说明要找的数字再右半部分
        #     if l % 3 == 0: left = r + 1
        #     #不能被3整除则说明要找的数字再左半部分
        #     else: right = l - 1
        # return nums[right]

        #位运算
        #考虑数字的二进制形式，对于出现三次的数字，各 二进制位 出现的次数都是 33 的倍数。因此，统计所有数字的各二进制位中 11 的出现次数，并对 33 求余，结果则为只出现一次的数字。
        # count_bits = [0]*32
        # for num in nums:
        #     i = -1
        #     while num != 0:
        #         count_bits[i] += num & 1
        #         num >>= 1
        #         i -= 1
        # bits = [str(c%3) for c in count_bits]
        # str_bits = ''.join(bits)
        # return int(str_bits, 2)
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)