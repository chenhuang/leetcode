'''
Interleaving String 

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

https://oj.leetcode.com/problems/interleaving-string/
'''

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        return self.isInterleaveRec(s1,s2,s3,0,0,0)

    def isInterleaveRec(self,s1,s2,s3,s1i,s2i,s3i):
        if s1i == len(s1) and s2i == len(s2) and s3i == len(s3):
            return True
        else:
            result = False
                #print s1i,s2i,s3i,s1[s1i],s2[s2i],s3[s3i]
            if s1i < len(s1) and s3i < len(s3):
                if s3[s3i] == s1[s1i]:
                    result = result or self.isInterleaveRec(s1,s2,s3,s1i+1,s2i,s3i+1)
            if s2i < len(s2) and s3i < len(s3):
                if s3[s3i] == s2[s2i]:
                    result = result or self.isInterleaveRec(s1,s2,s3,s1i,s2i+1,s3i+1)
            
        return result
        
if __name__ == "__main__":
    s = Solution()
    print s.isInterleave("aabcc","dbbca","aadbbcbcac")
    print s.isInterleave("aabcc","dbbca","aabccdbbca")
    print s.isInterleave("aabcc","dbbca","aadbbbaccc")
