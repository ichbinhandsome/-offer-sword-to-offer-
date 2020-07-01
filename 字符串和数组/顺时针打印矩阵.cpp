/*
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

 

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
*/
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        if(matrix.empty()) return ans;
        int l = 0, r = matrix[0].size() - 1, t = 0, b = matrix.size() - 1;
        int size = matrix[0].size() * matrix.size();
        while(true)
        {
            for(int i = l;i <= r;i++) ans.push_back(matrix[t][i]); //从左到右遍历
            t++;
            if(t > b) break; //往内“缩小一圈” 到top > bottom 时break
            for(int i = t;i <= b;i++) ans.push_back(matrix[i][r]); //上到下遍历
            r--;
            if(r < l) break; //“缩小”， 到right < left时break
            for(int i = r;i >= l;i--) ans.push_back(matrix[b][i]); //右到左遍历
            b--;
            if(b < t) break; //“缩小”， 到bottom < top 时break
            for(int i = b;i >= t;i--) ans.push_back(matrix[i][l]); //下到上遍历
            l++;
            if(l > r) break;//“缩小”， 到left > right时break
        }
        return ans;
    }
};
