'''
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

请写一个函数，求任意第n位对应的数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0
 

限制：

0 <= n < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
'''
class Solution:
    def findNthDigit(self, n: int) -> int:
        #计算第n个元素所在的数的数位为digit
        digit = 1
        #计算第digit数位元素的初始num: 1, 10, 100 ...
        start = 1
        # 总数位数
        count = 9
        while n > count:
            n -= count
            digit += 1
            start *= 10
            #经过的总的数位
            count = 9 * start * digit
        #第n个元素所在的数字
        num = start + (n-1)//digit
        #第n个元素在num中的第几位
        index = (n-1)%digit
        #得到n对应的元素
        return int(str(num)[index])
