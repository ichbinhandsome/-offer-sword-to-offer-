'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？


示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
'''
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        #BFS
        queue = [(0,0)]
        visited = set()
        visited.add((0,0))
        while queue:
            i,j = queue.pop(0)
            #left
            if j-1 >= 0:
                num = sum([int(n) for n in str(i)+str(j-1)])
                if num <= k and (i,j-1) not in visited:
                    queue.append((i,j-1))
                    visited.add((i,j-1))
            #right
            if j+1 < n:
                num = sum([int(n) for n in str(i)+str(j+1)])
                if num <= k and (i,j+1) not in visited:
                    queue.append((i,j+1))
                    visited.add((i,j+1))
            #up
            if i-1 >= 0:
                num = sum([int(n) for n in str(i-1)+str(j)])
                if num <= k and (i-1,j) not in visited:
                    queue.append((i-1,j))
                    visited.add((i-1,j))
            #down
            if i+1 < m:
                num = sum([int(n) for n in str(i+1)+str(j)])
                if num <= k and (i+1,j) not in visited:
                   queue.append((i+1,j))
                   visited.add((i+1,j))
        return len(visited)
###############################################################################
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        #DFS
        def dfs(i, j):
            if (i, j) in self.visited or i < 0 or i >= m or j < 0 or j >= n:
                return
            self.visited.add((i, j))
            if sum(map(lambda a: int(a), str(i) + str(j))) <= k:
                self.cnt += 1
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)
        self.visited = set()
        self.cnt = 0
        dfs(0, 0)
        return self.cnt
