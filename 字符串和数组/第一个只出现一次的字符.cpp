/*
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = "" 
返回 " "

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof
*/
class Solution {
public:
    char firstUniqChar(string s) {
        if (!s.size()) return ' ';
        unordered_map<char, int> hash_table;
        for (char i : s){
            hash_table[i]++;
        }
        for (int i = 0; i< s.size(); i++){
            if (hash_table[s[i]]==1) return s[i];
        }
        return ' ';
    }
};