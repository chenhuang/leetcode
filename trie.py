#! /usr/bin/python

class Solution:
    def __init__(self):
        self.tree = {}
        return

    def trie(self, words):
        for word in words:
            self.insert_tree(word)

    def print_trie(self):
        print self.tree

    def insert_tree(self, word):
        node = self.tree
        for i in word:
            if i not in node.keys():
                node[i] = {}
            node = node[i]
        if 'val' not in node.keys():
            node['val'] = 0
        node['val'] += 1

    def lookup_tree(self, word):
        node = self.tree
        for i in word:
            if i in node.keys():
                node = node[i]
            else:
                return 0
        if 'val' not in node.keys():
            return 0
        else:
            return node['val']

    def print_hints(self, word):
        node = self.tree
        for i in word:
            if i in node.keys():
                node = node[i]
            else:
                return None

        output = self.auto_complete(node)
        for i in range(len(output)):
            output[i] = word+output[i]
        return output
            
    def auto_complete(self, node):
        output = []
        for key in node.keys():
            if key != 'val':
                post_fix = self.auto_complete(node[key])
                for word in post_fix:
                    output.append(key+word)
            else:
                output.append("")
        return output

if __name__ == "__main__":
    s = Solution()
    s.trie(["apple","amazon","book","app","google"])
    s.insert_tree("dropbox")
    print s.print_hints("a")
    print s.print_hints("b")
    print s.print_hints("x")

