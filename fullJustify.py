#! /usr/bin/python

'''
Text Justification

Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
'''

# Greedy algorithm should do it. 
# 1. Determine the words to put into a line.
# 2. Determine the space between words
# 3. If it's the last line, left justifiy the line. 

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        line_len = 0
        line_words = []
        i = 0
        output = []

        while i < range(len(words)):
            while line_len <= L and i < range(len(words)):
                len_word = len(words[i])
                if line_len == 0:
                    line_len += len_word
                else:
                    line_len += 1 + len_word
                line_words.append(words[i])
                i += 1
            if line_len > L:
                extra_word = line_words.pop()
                line_len = line_len-len(extra_word)-1
                if len(line_words) == 1:
                    line = line_words[0]
                    while line_len < L:
                        line += " "
                        line_len += 1
                    output.append(line)
                else:
                    padding_num = (L-line_len)/(len(line_words)-1)
                    extra_paddings_num = (L-line_len)%(len(line_words)-1)
                    padding = ""

                    while padding_num > 0:
                        padding += " "
                        padding_num -= 1
                    
                    line = ""
                    for word in line_words:
                        line += word+" "
                        line += padding
                        if padding_num > 0:
                            line += " "
                            padding_num -= 1
                    line = line.rstrip()
                    output.append(line)

                line_len = 0

        return output

if __name__ == "__main__":
    s = Solution()
    print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)

