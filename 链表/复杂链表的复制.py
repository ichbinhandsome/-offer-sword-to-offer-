'''
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

 

示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 

提示：

-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return

        # #深拷贝的实现
        # #hash table + iterative
        # visited = {} #原节点：拷贝后的节点
        visited = {None:None}
        #先存储链表中所有的节点visited
        temp = head
        while temp:
            nd = Node(temp.val)
            visited[temp] = nd
            temp = temp.next
        t = head
        #再次遍历，为visited中拷贝的节点赋予next和random
        while t:
            #进行判断，因为visited中不存有None,而t.next and t.random 可能为None
            #如果visited已经存储None，则不需要再进行判断
            # if t.next:
            visited[t].next = visited[t.next]
            # if t.random:
            visited[t].random = visited[t.random]
            t = t.next
        return visited[head]

        #DFS 将来链表结构看作图
        visited = {}
        def dfs(node):
            if not node: return None
            if node in visited: return visited[node]
            nd = Node(node.val)
            visited[node] = nd
            nd.next = dfs(node.next)
            nd.random = dfs(node.random)
            return nd
        return dfs(head)

        #BFS
        #初始化
        visited = {head:Node(head.val)}
        queue = [head]

        while queue:
            node = queue.pop(0)

            if node.next and node.next not in visited:
                visited[node.next] = Node(node.next.val)
                queue.append(node.next)

            if node.random and node.random not in visited:
                visited[node.random] = Node(node.random.val)
                queue.append(node.random)
            
            visited[node].next = visited[node.next] if node.next in visited else None
            visited[node].random = visited[node.random] if node.random in visited else None
            
        return visited[head]








