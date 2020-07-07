'''
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

 

示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
 

提示：

各函数的调用总次数不超过 20000 次
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof
'''
class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        #使用辅助栈维护一个按插入顺序大小排列的栈
        self.helper = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        #插入时进行判断，是否将元素也插入到辅助栈中
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)


    def pop(self) -> None:
        n = self.stack.pop()
        if n == self.helper[-1]: self.helper.pop()



    def top(self) -> int:
        return self.stack[-1]


    def min(self) -> int:
        return self.helper[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()