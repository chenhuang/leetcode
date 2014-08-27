#! /usr/bin/python


class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    # Looks like a DFS problem, use recursion should be fine.
    def combinationSum2_1(self, candidates, target):
        candidates = sorted(candidates)
        self.output = []
        self.combinationSum2Rec(candidates,target,[],0)

        return self.output
        
    def combinationSum2Rec_1(self, candidates, target, recorded,start):
        for i in range(start,len(candidates)):
            if target == 0:
                if recorded not in self.output:
                    self.output.append(recorded)
            else:
                self.combinationSum2Rec(candidates[1:],target-i,recorded+[])

    def combinationSum2(self, candidates, target):
        result = []
        self.combinationSumRecur(sorted(candidates), result, [], 0, target)
        return result
        
    def combinationSumRecur(self, candidates, result, current, start, target):
        if target == 0 and current not in result:
            result.append(current)
        else:
            while start < len(candidates) and candidates[start] <= target:
                self.combinationSumRecur(candidates, result, current + [candidates[start]], start + 1, target - candidates[start])
                start += 1

    def combinationSum2_2(self, C,T):
        C = sorted(C)
        result = self.comb_sum_rec(C,T)
        return result

    def comb_sum_rec(self, C,T):
        result = []
        for i in range(len(C)):
            if i-1>=0 and C[i] == C[i-1]:
                continue
            else:
                if C[i] == T:
                    result.append([C[i]])
                if i+1 < len(C) and C[i+1] <= T-C[i]:
                    tmp_res = self.comb_sum_rec(C[i+1:],T-C[i])
                    for res in tmp_res:
                        result.append([C[i]]+res)
        return result
            
if __name__ == "__main__":
    s = Solution()
    print s.combinationSum2([10,1,2,7,6,1,5],8)
    print s.combinationSum2_2([10,1,2,7,6,1,5],8)
        
