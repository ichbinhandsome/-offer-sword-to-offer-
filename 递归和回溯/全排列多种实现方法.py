#全排列的多种实现方法

#DFS 递归
per = set()
def permutation(s, temp = ''):
    s = list(s)
    if len(s) == 0 :
        per.add(temp)
        return
    for i in range(len(s)):
        new = s[:]
        new.pop(i)
        permutation(new, temp+s[i])
permutation('abca')
print(per)

#回溯 + 交换
def allpermutation(s, start, end, result=set()):
    # result 是set（不可变对象） 所以不会改变 
    if start == end:
        result.add(''.join(s))
        return
    for i in range(start, end):
        s[i], s[start] = s[start], s[i]
        allpermutation(s, start+1,end, result)
        s[i], s[start] = s[start], s[i]
    return result
s = ['1','2','3']
end  = len(s)
print(allpermutation(s,0,end))


def solve(nums, start, end, res = []):
    if start == end:
        res.append(nums)
        return
    for i in range(start, end):
        if i != start and nums[i] == nums[start]: continue 
            #注意list是可变对象， 在修改的过程中一直在变化
            #需要使用copy函数 构造新的list
        nums[i], nums[start] = nums[start], nums[i]
        solve(nums, start+1, end, res)
        nums[i], nums[start] = nums[start], nums[i]

    return res

ex = [1,2,1,1]
ex.sort()
print(solve(ex,0,4))

'''
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
'''