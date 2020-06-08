'''
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
'''
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        #分组与或
        #思路：先计算出列表中所有元素的与或和s, 可知s也是unique元素p和q的与或
        #在s中找到一个标记位flag， 选择最后一个bit 1在s中出现的位置
        #这个位置说明p和q在这个位置上的bit不相等， 一个为0 另一个为1
        #以这个位置将数组中的元素分成两组, 这样一个组中含有p另一个含有q
        #将这两组元素分别进行与或操作， 这样就分别得到p和q
        s = 0
        for num in nums:
            s ^= num
        flag = 1
        while s & flag == 0:
            flag <<= 1
        # 0和任何数的与或都是那个数本身
        p, q  = 0, 0
        for num in nums:
            if  num & flag :
                p ^= num
            else:
                q ^= num
        return [p,q]
