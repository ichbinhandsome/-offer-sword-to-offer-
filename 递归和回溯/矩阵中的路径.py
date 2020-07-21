'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
提示：

1 <= board.length <= 200
1 <= board[i].length <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #DFS + 回溯 
        visited = [ [False]*len(board[0]) for i in range(len(board))]

        def dfs(word, index, i ,j, visited):
            #递归终止条件
            if i <0 or i >= len(board) or j <0 or j >= len(board[0]): return False
            if board[i][j] != word[index] or visited[i][j]: return False
            if index == len(word)-1: return True
            #设置访问后元素为ture 为的是不走回头路
            visited[i][j] = True
            #DFS依次遍历 下 右 左 上
            res =  dfs(word, index+1, i+1, j, visited) or dfs(word, index+1, i, j+1, visited) or dfs(word, index+1, i-1, j, visited) or dfs(word, index+1, i, j-1, visited)
            #回溯（必须） 为了下次的递归过程不被影响
            visited[i][j] = False
            return res
        #逐个点进行遍历
        for i in range(len(board)):
            for j in range(len(board[0])):
                #短路操作进行剪枝
                if board[i][j] == word[0] and dfs(word, 0, i,j, visited):
                    return True
        return False
