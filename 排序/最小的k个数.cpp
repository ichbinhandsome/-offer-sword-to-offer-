/*
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
*/
class Solution {
public:
    int partition(vector<int>&arr,int l,int r){
        int temp = arr[l];
        while( l < r){
            while( l < r && arr[r] >= temp) r--;
            arr[l] = arr[r];
            while(l < r && arr[l] <= temp) l++;
            arr[r] = arr[l]; 
        }
        arr[l] = temp;
        return l;
    }
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        //优先级队列
    //     priority_queue<int> heap; //大顶堆
    //     vector<int> res;
    //     for (int c : arr){
    //        heap.push(c);
    //        if (heap.size() > k) heap.pop();
    //     }
    //     while(!heap.empty()){
    //         res.push_back(heap.top());
    //         heap.pop();
    //     }
    //     return res;
    // }

    // quickselect
    int n=arr.size();
    if(n==k) return arr;
    if(n<k || k<=0 || n==0) return vector<int>();
    int l = 0,r = n-1;
    int index = partition(arr,l,r);
    while(index!=k-1){
        if(index>k-1) r=index-1;
        else l=index+1;
        index=partition(arr,l,r);
    }
    return vector<int>(arr.begin(),arr.begin()+k);
    }
};