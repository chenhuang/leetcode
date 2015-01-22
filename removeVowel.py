#! /usr/bin/python

class Solution:
    def __init__(self):
        pass

    def swap(self, chars, ptr, i):
        if ptr == i:
            return
        else:
            chars[ptr] = chars[i]

    def removeVowel(self, chars):
        ptr = 0
        vowel = ['a','e','i','o','u']

        for i in range(len(chars)):
            if chars[i] not in vowel:
                self.swap(chars,ptr,i)
                ptr += 1
                
        return chars[0:ptr]

if __name__ == "__main__":
    s = Solution()
    print s.removeVowel(['p','e','e','p','e','r','s'])
                
            
