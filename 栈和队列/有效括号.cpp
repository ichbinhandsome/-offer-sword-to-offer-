/*
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
*/
class Solution {
public:
    bool isValid(string s) {
        unordered_map<char,int> map= {{'(',1}, {'[', 2}, {'{', 3}, {')',4},{']',5}, {'}', 6}};
        stack<char> c;
        for (char i : s){
            if (map[i] >= 1 && map[i] <= 3) c.push(i);
            else if (!c.empty() && map[i]-3==map[c.top()]) c.pop();
            else return false;
        }
        return c.empty();
    }
};