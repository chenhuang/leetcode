#! /usr/bin/python

class Solution:
    def wordPattern(self, input_str, pattern):
        itms = input_str.split(" ")
        mapping = {}

        for i in range(len(itms)):
            itm = itms[i]
            pat = pattern[i]
            
            if pat not in mapping.keys():
                mapping[pat] = itm
            else:
                if itm != mapping[pat]:
                    return False

        return True

    def harderWordPattern(self, input_str, pattern):
        #return self.searchPattern(input_str, pattern, {})
        return self.searchPattern1(input_str, pattern, {})

    def searchPattern(self, input_str, pattern, pat2word):
        if len(input_str) == 0 and len(pattern) == 0:
            return True
        else:
            pat = pattern[0]

            if pat in pat2word.keys():
                word = pat2word[pat]
                if input_str[0:len(word)] == word:
                    result = self.searchPattern(input_str[len(word):], pattern[1:], dict(pat2word))
                    if result == True: return True
            else:
                for i in range(1, len(input_str)):
                    word = input_str[0:i]
                    pat2word[pat] = word
                    result = self.searchPattern(input_str[i:], pattern[1:], dict(pat2word))
                    if result == True: return True

            return False

    def searchPattern1(self, input_str, pattern, pat2word):
        str_pos = 0
        for i in range(len(pattern)):
            pat = pattern[i]

            if pat in pat2word.keys():
                word = pat2word[pat]
                if input_str[str_pos:str_pos+len(word)] != word:
                    return False
                else:
                    str_pos += len(word)
            else:
                for j in range(str_pos+1, len(input_str)):
                    word = input_str[str_pos:j]
                    pat2word[pat] = word
                    result = self.searchPattern(input_str[str_pos:], pattern[i:], dict(pat2word))
                    if result == True: return True

        if str_pos == len(input_str):
            return True
        else:
            return False



if __name__ == "__main__":
    s = Solution()

    #print s.wordPattern('dog cat cat dog',['a','b','b','a'])
    #print s.wordPattern('dog cat cat dog',['a','b','b','b'])
    print s.harderWordPattern('dogcatcatdog',['a','b','b','a'])
    print s.harderWordPattern('dogcatcatdog',['a','b','b','b'])
    print s.harderWordPattern('abbbbbba',['a','b','b','a'])



