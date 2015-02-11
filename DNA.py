class Solution:
    # @param s, a string
    # @return a list of strings
    # ACTG: 1234
    class Trie:
        def __init__(self):
            self.tree = {}
            
        def is_exist(self, string):
            node = self.tree
            for i in string:
                if i not in node.keys():
                    node[i] = {}
                node = node[i]
            if 'END' not in node.keys():
                node['END'] = 1
                return False
            else: 
                node['END'] += 1
                if node['END'] == 2:
                    return True
                else:
                    return False

    def findRepeatedDnaSequences(self, s):
        check = Solution.Trie()
        output = []
        for i in range(0,len(s)-10):
            if check.is_exist(s[i:i+10]):
                output.append(s[i:i+10])
        return output
class Solution:
    # @param s, a string
    # @return a list of strings
    # ACTG: 1234
    class Trie:
        def __init__(self):
            self.tree = {}
            
        def is_exist(self, string):
            node = self.tree
            for i in string:
                if i not in node.keys():
                    node[i] = {}
                node = node[i]
            if 'END' not in node.keys():
                node['END'] = 1
                return False
            else: 
                node['END'] += 1
                if node['END'] == 2:
                    return True
                else:
                    return False

    def findRepeatedDnaSequences(self, s):
        check = Solution.Trie()
        output = []
        for i in range(0,len(s)-10):
            if check.is_exist(s[i:i+10]):
                output.append(s[i:i+10])
        return output

if __name__ == "__main__":
    s = Solution()
    print s.findRepeatedDnaSequences('AAAAAAAAAAAAA')
