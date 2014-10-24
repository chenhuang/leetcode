#! /usr/bin/python

class Solution:
    def bfs(self, source, target, dictionary):
        queue = []
        queue.append(source)
        parents = {}

        while len(queue) > 0:
            word = queue.pop(0)

            for i in range(len(word)):
                char_i = word[i]
                for j in range(ord('a'),ord('z')+1):
                    if j == ord(char_i):
                        continue
                    new_word = word[:i]+str(chr(j))+word[i+1:]
                    if new_word in dictionary and new_word not in parents.keys():
                        queue.append(new_word)
                        parents[new_word] = word
                    if new_word == target:
                        steps = 3
                        parent = parents[word]
                        while parent != source:
                            parent = parents[parent]
                            steps += 1
                        return steps

        return 0
            
if __name__ == "__main__":
    s = Solution()
    source = "hit"
    target = "cog"
    dic = ["hot","dot","dog","lot","log"] 
    print s.bfs(source, target, dic)
