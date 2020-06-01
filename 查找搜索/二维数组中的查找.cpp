/*
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof
*/
class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        //右上角开始
        if (matrix.empty()){
            return false;
        }
        int row = matrix.size();
        int col = matrix[0].size();
        int i = 0, j = col-1;
        while (i<row && j>-1){
            if (matrix[i][j] == target){
                return true;
            }else if (matrix[i][j]>target){
                j--;
            }else{
                i ++;
            }
        }
        return false;

    }
};