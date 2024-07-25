class Solution:
    def sortArray(self, nums):
        def mergeSort(nums, l, r):
            if l >= r:
                return

            m = (l + r) // 2

            mergeSort(nums, l, m)
            mergeSort(nums, m + 1, r)

            merge(nums, l, m, r)

        def merge(nums, l, m, r):
            left = nums[l : m + 1]
            right = nums[m + 1 : r + 1]

            leftIndex = 0
            rightIndex = 0
            mergeIndex = l

            while leftIndex < len(left) and rightIndex < len(right):
                if left[leftIndex] <= right[rightIndex]:
                    nums[mergeIndex] = left[leftIndex]
                    leftIndex += 1
                else:
                    nums[mergeIndex] = right[rightIndex]
                    rightIndex += 1
                mergeIndex += 1

            while leftIndex < len(left):
                nums[mergeIndex] = left[leftIndex]
                leftIndex += 1
                mergeIndex += 1

            while rightIndex < len(right):
                nums[mergeIndex] = right[rightIndex]
                rightIndex += 1
                mergeIndex += 1

        mergeSort(nums, 0, len(nums) - 1)
        return nums
