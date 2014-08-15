#! /usr/bin/env python

'''
Count and Say 

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

https://oj.leetcode.com/problems/count-and-say/
'''

class Solution:
    # @return a string
    def countAndSay(self, n):
        output = "1"
        for i in range(n-1):
            new_output = ""
            prev_j=""
            current_count = 0

            # Count
            for j in range(len(output)):
                if prev_j == "":
                    prev_j = output[j]
                    current_count += 1
                else:
                    if output[j] == prev_j:
                        current_count += 1
                    else:
                        new_output += str(current_count)+prev_j
                        prev_j = output[j]
                        current_count = 1
            output = new_output + str(current_count)+prev_j

        return output
            
if __name__ == "__main__":
    s = Solution()
    print s.countAndSay(3)
