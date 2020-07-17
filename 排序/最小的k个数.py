'''
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
'''
import heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        #小顶堆
        # heapq.heapify(arr)
        # return heapq.nsmallest(k,arr)

        #大顶堆
        #trick:使用负号， heapq模块只提供小顶堆
        # if k == 0: return []
        # res = []
        # heapq.heapify(res)
        # for i in range(len(arr)):
        #     if len(res) < k: heapq.heappush(res, -(arr[i]))
        #     else:
        #         if -(arr[i]) > res[0]:
        #             heapq.heappop(res)
        #             heapq.heappush(res, -(arr[i]))
        # return [-i for i in res]

        #快速排序中的快速选择
        def quickselect(nums, left, right, k):
            if left >= right: return 
            standard = nums[left]
            i = left
            j = right
            while i <= j:
                while (i <= j and nums[i] <= standard): i+=1
                while (i <= j and nums[j] >= standard): j -=1
                if (i <= j):
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            nums[j], nums[left] = nums[left], nums[j]

            if j > k :
                quickselect(nums, left, j-1, k)
            elif j < k:
                quickselect(nums, j + 1, right, k)
            return

        quickselect(arr, 0, len(arr)-1, k)
        return arr[:k]


        # def quickselect(arr, left, right, k):
        #     if left>=right: return
        #     pivot = arr[left]
        #     i , j = left, right
        #     while i <= j:
        #         while i <= j and arr[i] <= pivot:
        #             i += 1
        #         while j >= i and arr[j] >= pivot:
        #             j -= 1
        #         if i <= j:
        #             arr[i], arr[j] = arr[j], arr[i]
        #             i += 1
        #             j -= 1
        #     arr[left], arr[j] = arr[j], arr[left]

        #     if k == j: return
        #     elif k < j: quickselect(arr, left, j-1, k)
        #     else: quickselect(arr, j + 1, right, k)
    
        # quickselect(arr, 0, len(arr) - 1, k)
        # return arr[:k]