class Solution:
    def candy(self, n):
        length = len(n)
        candies = [1] * length
        for i in range(1, length ): #compare right element to its left neighbour
            if n[i] > n[i - 1]:
                candies[i] = candies[i - 1] + 1
        for x in range(length-2,-1,-1): #compare left element to its right neighbour
                  if n[x] > n[x + 1]:
                    if  candies[x] > candies[x+1]:
                          continue
                    else:
                        candies[x]=candies[x+1]+1
        return sum(candies)
n = [29,51,87,87,72,12]
solution = Solution()
solution.candy(n)