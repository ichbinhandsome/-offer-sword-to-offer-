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
