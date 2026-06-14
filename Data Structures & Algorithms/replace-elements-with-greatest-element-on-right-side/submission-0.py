class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        res = [-1]*l

        for i in range(l-2,-1,-1):
            res[i] = max(arr[i+1], res[i+1])
                
        return res