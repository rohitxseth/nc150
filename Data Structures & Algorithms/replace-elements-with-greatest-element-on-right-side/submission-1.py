class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n = arr.pop(-1)
        arr.append(-1)

        for i in range(len(arr)-2,-1,-1):
            j = arr[i]
            arr[i] = max(n,arr[i+1])
            n = j
        
        return arr
            