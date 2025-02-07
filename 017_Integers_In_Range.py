class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        sweeper = [0 for _ in range(52)]
        for [start, end] in ranges:
            sweeper[start] += 1
            sweeper[end + 1] -= 1
        sum = 0
        for i in range(0, right + 1):
            sum += sweeper[i]
            if i >= left and sum <= 0:
                return False
        
        return True
