class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordSegmentation(self, s, dict):
        # write your code here
        s_match = [False for i in range(len(s)+1)]
        s_match[0] = True
        for i in range(1, len(s)+1):
            for j in dict:
                if i - len(j) >= 0:
                    if s[i - len(j):i] == j:
                        if s_match[i - len(j)]:
                            s_match[i] = True

        return s_match[len(s)]

if __name__ == "__main__":
    s = Solution()
    print s.wordSegmentation("a", ["a"])
