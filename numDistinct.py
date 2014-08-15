#! /usr/bin/python

'''
Distinct Subsequences


Given a string S and a string T, count the number of distinct subsequences of T in S.
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE"while "AEC" is not).
Here is an example:
S = "rabbbit", T = "rabbit"
Return 3.
'''


class Solution:
    def numDistinct(self, S, T):
        self.count = 0
        self.numDistinctRec(S,T)
        return self.count

    def numDistinctRec(self, S, T):
        if S == T:
            self.count += 1
        else:
            for i in range(len(S)):
                new_S = S[:i]+S[i+1:]
                self.numDistinctRec(new_S, T)

# DP solution

    def numDistinct_DP(self, S, T):
        t = [[0] for i in range(len(T))]

        # Initialize:
        if T[0] == S[0]:
            t[0][0] = 1
        for i in range(1,len(S)):
            if T[0] == S[i]:
                t[0].append(t[0][i-1]+1)
            else:
                t[0].append(0)
        
        # Now filling out the matrix:
        for i in range(1, len(T)):
            for j in range(1, len(S)):
                if T[i] == S[j]:
                    t[i].append(t[i-1][j-1]+t[i][j-1]) # This is the key part very difficult the + part
                else:
                    t[i].append(t[i][j-1])
        print t

        return t[len(T)-1][len(S)-1]


if __name__ == "__main__":
    s = Solution()
    print s.numDistinct("rabbbit","rabbit")
    print s.numDistinct_DP("rabbbit","rabbit")

    
        

