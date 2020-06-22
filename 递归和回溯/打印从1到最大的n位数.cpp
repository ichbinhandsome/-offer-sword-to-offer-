/*
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof
*/


/*
回溯法的解体框架是什么呢，解决一个回溯问题，实际上就是一个决策树的遍历过程。一般来说，我们需要解决三个问题：

路径：也就是已经做出的选择。
选择列表：也就是你当前可以做的选择。
结束条件：也就是到达决策树底层，无法再做选择的条件。
我们所使用的框架基本就是：


LinkedList result = new LinkedList();
public void backtrack(路径，选择列表){
    if(满足结束条件){
        result.add(结果);
    }
    for(选择：选择列表){
        做出选择;
        backtrack(路径，选择列表);
        撤销选择;
    }
}
*/

class Solution {
public:
    vector<int> res;
    vector<int> printNumbers(int n) {
        if(n <=0 ) return res;
        string number(n,'0');
        for(int i = 0;i <= 9;i++)
        {
            number[0] = i + '0';
            permutionNum(number, n, 1);
        }
        return res;
    }

    void permutionNum(string &number, int length, int index)
    {
        if(index == length)
        {
            saveNum(number);
            return;
        }else
        {
            for(int i=0;i<10;i++)
            {
                number[index] = '0' + i;
                permutionNum(number,length,index+1);
            }
        }
    }
    void saveNum(string number)
    {
        string tempStr(number.size(),'0');
        // std::cout<< stoi(number) <<" ";
        if(number!=tempStr)
        res.push_back(stoi(number));
    }
};


