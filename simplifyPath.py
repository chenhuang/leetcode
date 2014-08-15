#! /usr/bin/python

'''
Simplify Path

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

https://oj.leetcode.com/problems/simplify-path/
'''

class Solution:
    # @param path, a string
    # @return a string
    # Feels like a stack problem
        
    def simplifyPath(self, path):
        path_stack = []
        path_array = path.split("/")
        
        for i in path_array:
            if i == '.':
                continue
            elif i == '..':
                if len(path_stack) > 0:
                    path_stack.pop()
            elif i=="":
                continue
            else:
                path_stack.append(i)

        return "/"+"/".join(path_stack)


if __name__ == "__main__":
    s = Solution()
    print s.simplifyPath("/home/")
    print s.simplifyPath("/a/./b/../../c/")
