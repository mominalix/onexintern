class Solution(object):
    import bisect

    def maxEnvelopes(self,envelopes):
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for envelope in envelopes:
            idx = bisect.bisect_left(dp, envelope[1])
            if idx == len(dp):
                dp.append(envelope[1])
            else:
                dp[idx] = envelope[1]
        return len(dp)
envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
solution=Solution()
solution.maxEnvelopes(envelopes)
