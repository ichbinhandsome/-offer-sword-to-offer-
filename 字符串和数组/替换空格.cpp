/*
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof
*/
class Solution {
public:
    string replaceSpace(string s) {
        //双指针 inplace operation
        int len = s.size();
        if (len==0){
            return s;
        }
        int space = 0;
        int i = s.size(); //first pointer
        auto si = s.begin();
        //count how many white space
        while (si!=s.end()){
            if (*si ==' '){
                ++space;
            }
            ++si;
        }
        s.resize(s.size()+2*space);
        int j = s.size();//second pointer
        while (i!=j){
            if (s[i]!= ' '){
                s[j--] = s[i];
            }else{
                s[j--] = '0';
                s[j--] = '2';
                s[j--] = '%';
            }
            --i;
        }
        return s;
    }
};