#! /usr/bin/env python

'''
Edit Distance 

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

https://oj.leetcode.com/problems/edit-distance/
'''

class Solution:
    # @return an integer
    # DP problem:
    # word1 -> word2, 
    # if i != j:
    #   steps[i][j] = min(steps[i-1][j] + 1 delete,
    #   steps[i][j-1] + 1 insert,
    #   steps[i-1][j-1] + 1 replace)
    def minDistance_1(self, word1, word2):
        steps = []
        length = max(len(word1),len(word2))
        steps = [[] for i in range(length)]
        if word1[0] == word2[0]:
            steps[0][0] = 0
        else:
            steps[0][0] = 1

        for i in range(1,len(word2)):
            steps[0].append(steps[0][i-1]+1)
            
        for i in range(1,len(word1)):
            steps[i].append(i)

        for i in range(1,length):
            steps[i].append(i) #Deletion
            steps[0].append(i) #Insertion

        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                if word1[i] == word2[j]:
                    steps[i].append(steps[i-1][j-1])
                else:
                    steps[i].append(min(steps[i-1][j]+1, steps[i][j-1]+1, steps[i-1][j-1]+1))
        print steps
        return steps[len(word1)-1][len(word2)-1]

    def minDistance(self, word1, word2):
        distance = [[i] for i in range(len(word1)+1)]
        distance[0] = [i for i in range(len(word2)+1)]
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                deletion = distance[i-1][j]+1
                addition = distance[i][j-1]+1
                substitution = distance[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    substitution += 1
                distance[i].append(min(deletion, addition, substitution))
        return distance[-1][-1]


if __name__ == "__main__":
    s = Solution()
    print s.minDistance("acd","abcd")
      

        
