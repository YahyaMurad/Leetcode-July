class Solution:
    def frequencySort(self, nums):
        freq = [0 for i in range(201)]
        for num in nums:
            freq[num + 100] += 1

        nums.sort(key=lambda val: (freq[val + 100], -val))
        return nums