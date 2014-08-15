#! /usr/bin/python


def dex_26_iter(s):
	output = ""
	while s/2 != 0:
		output = str(s%2) + ' ' + output
		s = s/2

	output = str(s%2)+ ' ' + output
	return output
		
def dex_26_rec(s):
	if s/26 == 0:
		return str(s%26)
	else:
		return dex_26_rec(s/26) + str(s%26)

print dex_26_rec(52)
		
