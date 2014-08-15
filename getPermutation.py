#! /usr/bin/python

'''
Permutation Sequence 


By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

https://oj.leetcode.com/problems/permutation-sequence/
'''

class Solution:
    # @return a string
    def getPermutation_1(self, n, k):
        permutations = [[]] 
        count = 0
        for i in range(1,n+1):
            next = []
            for j in permutations:
                for l in range(len(j)+1):
                    s = j[:l] + [i] + j[l:]
                    next.append(s)
            #        count += 1
            #        if count==k:
            #            return j
            permutations = next
        return permutations

    def getPermutation(self,n,k):
        self.output = []
        self.getPermutationRec(n,k,[i+1 for i in range(n)],0,0)
        return self.output[k-1]
        


    def getPermutationRec(self,n,k,num,start,count):
        if start == n:
            print num
            self.output.append(num)
        else:
            for i in range(start,n):
                a = num[start]
                b = num[i]
                num[i] = a
                num[start] = b
                self.getPermutationRec(n,k,list(num),start+1,count)
                num[i] = b
                num[start] = a
            


if __name__ == "__main__":
    s = Solution()
    print s.getPermutation(4,5)
