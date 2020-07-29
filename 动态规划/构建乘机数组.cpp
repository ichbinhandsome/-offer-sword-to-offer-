/*
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

 

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof
*/

class Solution {
public:
    vector<int> constructArr(vector<int>& a) {
        int n = a.size();
        vector<int> L (n,1);
        vector<int> R (n,1);
        for (int i = 1; i < n; i++){
            L[i] = L[i-1] * a[i-1];
        }
        for (int j = n-2; j > -1; j--){
            R[j] = R[j+1] * a[j+1];
        }
        for (int i = 0; i < n; i++){
            L[i] = L[i] * R[i];
        }
        return L;
        
    }
};