from collections import defaultdict as dict
from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound
class RangeFreqQuery:
    
    def __init__(self, arr):
        self.store = dict(list)    
        n = len(arr)
        for i in range(n):
            self.store[arr[i]].append(i)   
    def query(self, left: int, right: int, value: int) -> int:
        a = lower_bound(self.store[value], left)
        b = upper_bound(self.store[value], right)
    
        return b - a
