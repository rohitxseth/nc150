class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        smallest = min(nums)
        total = 0

        while smallest:
            total = total + smallest % 10
            smallest = smallest // 10

        return 1 - total % 2
