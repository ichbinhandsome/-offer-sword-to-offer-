'''
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

 

示例:

输入: a = 1, b = 1
输出: 2
 

提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof
'''
class Solution:
    def add(self, a: int, b: int) -> int:
        #python 比较特殊 没有补码 所以说对于负数 要将其转化
        x = 0xffffffff
        a, b = a & x, b & x
        #终止条件 当b==0
        while b != 0:
            #计算无进位数字 异或
            #计算进位数字 与 左移1位
            a, b = (a ^ b), (a & b) << 1 & x
        #判断a是否小于0 大于0直接返回 小于0 ~(a ^ x)
        return a if a <= 0x7fffffff else ~(a ^ x)