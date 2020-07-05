/*
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

 

示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1
 

限制：

1 <= nums.length <= 10000
1 <= nums[i] < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-ii-lcof
*/


/*  
            ab    ab    ab    ab
    状态机: 00 -> 01 -> 10 -> 00
    真值表:
    c   b   a   b'
    0   0   1   0
    0   0   0   0
    0   1   1   0
    0   1   0   1
    1   0   1   0
    1   0   0   1
    1   1   1   0
    1   1   0   0
    取结果为1的情况：b' = ~ab~c + ~a~bc = ~a(b~c+~bc) = ~a(b^c)
    因此，可以推出: b = b ^ c & ~a

    在更新b之后：
            ab    ab    ab    ab
    状态机: 01 -> 00 -> 10 -> 01
    调换ab: ba    ba    ba    ba
    状态机: 10 -> 00 -> 01 -> 10
    与上述一致，因此，可以推出：a = a ^ c & ~b

*/
class Solution {
public:
    int singleNumber(vector<int>& nums) {
    //     int a = 0, b = 0;
    //     for (int c: nums) {
    //         b = b ^ c & ~a;
    //         a = a ^ c & ~b;
    //     }
    //     return b;
    // }

    /*
    用一个数组统计1的数目*/
    vector<int> bits(32,0);
    const int m = 3;
    for (int num: nums){
        int index = 0;
        while (num!=0){
            bits[index++] += num & 1;
            num /= 2;
        }
    }
    int b = 0, res = 0;
    for (int bit:bits){
        bit = bit % 3;
        res |= bit << b;
        ++b;
    }
    return res;
    }
};
