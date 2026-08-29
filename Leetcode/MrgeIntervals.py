class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])

        result = []

        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result
    
n = int(input("Enter number of intervals: "))

intervals = []

for i in range(n):
    start, end = map(int, input(f"Enter interval {i + 1}: ").split())
    intervals.append([start, end])


solution = Solution()

print(solution.merge(intervals))
    