#! /usr/bin/python
# Identify and find all subsets of a set

# Recursive
# This is a first attempt, being stupid version I made to recursively solve subset problem
def find_subsets_recursive_1(s):
	if len(s) == 1:
		return s
	else:
		for i in s:
			j = set(s)
			k = find_subsets_recursive(j.remove(i))
			return k.add(i)

# The recursion solution has been called as the recursie back tracking solution
# This solution has been acknowledged to be not so obvious to novice
# Subtle points:
# 1. how to keep invariant across the recursion
# 2. how to backtrack
# 3. how to copy by value
# Conclusion: this is indeed an ugly algorithm and should be avoid in the future. 
def subsets_rec(s):
  output = []
  temp = []
  for i in range(len(s)):
    find_subsets_recursive(s,i,output,temp)
  return output
  
def find_subsets_recursive(s,pos,output,temp):
#  print temp,pos
  if pos == len(s):
    output.append([list(temp)])
    return
  temp.append(s[pos])
  find_subsets_recursive(s,pos+1,output,temp)
  temp.pop()
  if len(temp) > 0:
    output.append([list(temp)])
  #find_subsets_recursive(s,pos+1,output,temp)

# Recursion with generator
def find_subsets_recursive(s):
  if len(s) == 1:
    yield s 
  else:
    for i in range(len(s)):
      yield [s[i]]
      if s[i+1:]:
        for j in find_subsets_recursive(s[i+1:]):
          yield [s[i]]+j

# Very nice solution, I have never thought of this before: 
# This is actually the DP/Greedy solution right: else contains the intial status, and each iteration increment the element in the set, very nice solution...
def subsets_iter(S):
    print '\nSubsets of', S
    S = sorted(S)
    ss = []
    for ch in S:
        if ss:
            ss += [sset + [ch] for sset in ss]
        else:
            ss.append([])
            ss.append([ch])
    print ss
    return ss

# Naive approach
def find_subsets_iterative(s):
	output = []
	output_sets = []
	for i in range(len(s)+1):
		if i == 0:
			output.append([set()])
			output_sets.append(set())
		else:
			output.append([])
			for j in s:
				for k in output[i-1]:
					l = set(k)
					if j not in l:
						l.add(j)
						if l not in output[i]:
							output[i].append(l)
							output_sets.append(l)
	return output_sets
			
#print find_subsets_iterative(set([1,2,3,4,5]))
for i in find_subsets_recursive([1,1]):
  print i
#subsets_iter([1,2,3,4,5])
#print subsets_rec([1,2,3,4,5])

