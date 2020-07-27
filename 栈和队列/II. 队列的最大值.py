'''
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入: 
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入: 
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
 

限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof
'''
class MaxQueue:
    
    def __init__(self):
        self.queue = collections.deque()
        self.deque = collections.deque()
    def max_value(self) -> int:
        if not self.queue: return -1
        return self.deque[0]


    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.deque and self.deque[-1] < value:
            self.deque.pop() 
        self.deque.append(value)

    def pop_front(self) -> int:
        if not self.queue: return -1
        front = self.queue.popleft()
        if front == self.deque[0]: self.deque.popleft()
        return front




# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()