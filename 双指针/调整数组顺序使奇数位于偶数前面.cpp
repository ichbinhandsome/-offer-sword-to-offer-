/*
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
 

提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof
*/
class Solution {
public:
    vector<int> exchange(vector<int>& nums) {
        int i = 0, j = nums.size()-1;
        while (i<j){
            while (i<j && nums[i] % 2 == 1) i++;
            while (j>i && nums[j] % 2 == 0) j--;
            swap(nums[i],nums[j]);
        }
        return nums;
    }
};