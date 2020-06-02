/*
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2
示例 2：

输入：n = 7
输出：21

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lco
*/
class Solution {
public:
    int numWays(int n) {
        // int dp[n+2];
        // dp[0] = 0;
        // dp[1] = 1;
        // for (int i =2; i <= n+1;i++){
        //     dp[i] = (dp[i-1]+dp[i-2] )% 1000000007 ;
        // }
        // return dp[n+1];
        if (n==0) return 1;
        int a = 0 , b =1;
        for (int i = 1; i <= n; i++ ){
            b = a + b;
            while (b > 1e9 + 7) b = b - 1e9-7, a = a - 1e9 - 7;
            a = b -a; 
        }
        return b;

    }
};