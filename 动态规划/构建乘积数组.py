'''
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

 

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
'''
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        #表格简易动态规划
       n = len(a)
       L, R = [1] * n, [1] * n
       for i in range(1, n):
           L[i] = L[i - 1] * a[i - 1]
       for j in reversed(range(n - 1)):
            R[j] = R[j + 1] * a[j + 1]
       for i in range(n):
            L[i] = L[i] * R[i]
       return L