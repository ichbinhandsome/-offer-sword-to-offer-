/*
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
*/

class Solution {
public:
    int minArray(vector<int>& numbers) {
        if (numbers.empty()) return 0;
        int left = 0, right = numbers.size()-1;
        while (left < right){
            int mid = (left+right)/2;
            if (numbers[mid] < numbers[right]) right = mid;
            else if (numbers[mid] > numbers[right]) left = mid+1;
            else{
                // 特殊情况，直接遍历查找最小值
                int res = numbers[left];
                for (int i = left; i<=right; i++){
                    if (numbers[i] < res) res = numbers[i];
                }
                return res;
            }
        }
        return numbers[left];
    }
};