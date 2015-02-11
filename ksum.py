class Solution:
    """
    @param A: An integer array.
    @param k: a positive integer (k <= length(A))
    @param target: integer
    @return an integer
    """
    def kSum(self, A, k, target):
        dp = [[0 for j in range(target+1)] for i in range(k+1)]
        dp[0][0] = 1

        def foo(i):print i
        for j in range(len(A)):
            #for p in range(target, A[j]-1, -1):
            for p in range(A[j], target+1):
                for i in range(1, k+1):
                    dp[i][p] += dp[i-1][p-A[j]]
                map(foo, dp)
                print j,p

        return dp[k][target]

if __name__ == "__main__":
    s = Solution()
#    print s.kSum([1,2,3,4,5,6,7],3,10)
    print s.kSum([1,2,3,4,5],2,6)
    #print s.kSum([1,4,6,8,10,13,15,17,18,21,23,26,27,28,29,30,32,35,36], 9, 133)
