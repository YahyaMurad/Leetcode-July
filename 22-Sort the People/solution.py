class Solution:
    def sortPeople(self, names, heights):
        return [name for name, _ in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)]
        