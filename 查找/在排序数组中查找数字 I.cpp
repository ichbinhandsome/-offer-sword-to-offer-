/*
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
*/
class Solution {
public:
    int search_right_boundary(vector<int> & nums, int target){
        int left = 0, right = nums.size();
        while(left < right){
            int mid = (left+right)>>1;
            (nums[mid] <= target)? left = mid+1: right = mid;
        }
        //此时 left = right
        return left;
    }
    int search(vector<int>& nums, int target) {
        //二分查找 查找target 和 target-1的右边界 两者相减即为所求
        return search_right_boundary(nums, target)- search_right_boundary(nums, target-1);
    }
};
