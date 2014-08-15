#! /usr/bin/python

'''Reverse Words in a String
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

http://oj.leetcode.com/problems/reverse-words-in-a-string/

* Clatification:
What constitutes a word?
A sequence of non-space characters constitutes a word.

Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.

How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
'''

def reverse_words(s):
	itms = s.split()
	rwords = []
	for i in itms:
		if len(i) != 0:
			rwords.insert(0,i)
	return " ".join(rwords)

