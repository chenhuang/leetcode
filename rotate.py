'''
Rotate Image 

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

https://oj.leetcode.com/problems/rotate-image/
'''

class Solution:
# @param matrix, a list of lists of integers
# @return a list of lists of integers
# two step process:
# 1. 

'''
123
456
789

flip:
147
258
369

flip:
741
852
963
'''   
    def rotate(self, matrix):
        a = zip(*matrix)
        b = [list(i) for i in a]
        for i in b:
            i.reverse()

        return b
