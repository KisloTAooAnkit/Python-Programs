from collections import defaultdict


def numPairsDivisibleBy60(self, arr) -> int:
    dic = defaultdict(int)
    n = len(arr)
    ans = 0
    for i in range(n):
        mod1 = arr[i] % 60
        if mod1 == 0:
            ans += dic[0]
            dic[mod1] += 1
            continue
        mod2 = 60-mod1
        ans += dic[mod2]
        dic[mod1] += 1
    return ans