/*
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

 

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
*/
class Solution {
public:
    double myPow(double x, int n) {
        if (x==0) return 0;
        if (n==0) return 1;
        long pow  = n;
        if (pow < 0){
            x = 1/x;
            pow = -pow;
        }
        double ans = 1;
        while (pow > 0){
            if (pow&1 == 1) ans *= x;
            x *= x;
            pow >>= 1;
        } 
        return ans;
    }
};