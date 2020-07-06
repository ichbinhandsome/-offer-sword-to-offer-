/*
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

 

示例 1：

输入: "the sky is blue"
输出: "blue is sky the"
示例 2：

输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 

说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof
*/

class Solution {
public:
    string reverseWords(string s) {
        int k = 0;
        for (int i = 0; i < s.size(); ++ i){
            while (i < s.size() && s[i] == ' ') ++i;  //找到第一个非空格字符
            if (i == s.size()) break;
            int j = i;
            while (j < s.size() && s[j] != ' ') ++j;    //遍历1个非空单词
            reverse(s.begin() + i, s.begin() + j);      //反转1个单词
            if (k) s[k++] = ' ';
            while (i < j) s[k++] = s[i++];      //反转后的1个单词赋给s[k]
        }
        s.erase(s.begin() + k, s.end());   //删除 k后面空格
        reverse(s.begin(), s.end());
        return s;
    }
};
