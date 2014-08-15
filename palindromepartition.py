#!/usr/bin/env python

'''
Palindrome Partitioning 

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]

https://oj.leetcode.com/problems/palindrome-partitioning/

-----

Palindrome Partitioning II 

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

https://oj.leetcode.com/problems/palindrome-partitioning-ii/
'''

class Solution:
    # @param s, a string
    # @return a list of lists of string
    # DFS
    def partition(self, s):
        self.output = []
        self.dfs(s,0,[])
        return self.output

    def dfs(self, s, start, records):
        if start == len(s):
            self.output.append(records)
        else:
            for i in range(start+1, len(s)+1):
                prefix = ''.join(s[start:i])
                if self.isPal(prefix):
                    records.append(prefix)
                    self.dfs(s,i,list(records))
                    records.pop()

    def isPal(self, s):
        s_len = len(s)
        for i in range(0, s_len/2):
            if s[i] != s[s_len-1-i]:
                return False

        return True

    # @param s, a string
    # @return an integer
    # The DP part is in the algorithm, the DP part is in the isPal
    # NOTE: This solution is problematic: see case: cabbacc
    # The problem is that I wrote the DP function wrong, the correct way is to write: 
    # min_cut(i,j) = min(min_cut(i,k)+min_cut(k,j), for k in range(i,j))
    # instead, what i wrote is min_cut(i,j) = min(min_cut(i)+i-j,min_cut(j)), min(min_cut(j),min_cut(i)), the problem is that I wrote the transfer function wrong.
    # min_cut(

    def minCut(self, s):
        cuts = []
        pal = []

        for i in range(len(s)):
            cuts.append(i)

        for i in range(1,len(s)):
            for j in reversed(range(i)):
                if self.isPal_1(s,j,i,pal):
                    cuts[i] = min(cuts[i],cuts[j]+1)

                #print i,j,cuts,s[j:i+1],self.isPal_1(s,j,i,pal)
        return cuts[len(s)-1]

    def isPal_1(self, s, i, j, pal):
        for k in range(i, (i+j+1)/2):
            if s[k] != s[(i+j)-k]:
                return False

        return True
        

if __name__ == "__main__":
    s = Solution()
    #print s.partition("aab")
    print s.minCut("cabbacc")
    print s.minCut("cabbac")
    print s.minCut("abc")
    print s.minCut("aaa")

