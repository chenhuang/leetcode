#! /usr/bin/env python

def permutation(ilist,i,output):
    if i < len(ilist)-1:
        a = ilist[i]

        for j in range(i,len(ilist)):
            tmp = ilist[j]
            ilist[j] = a
            ilist[i] = tmp
            new_list = list(ilist)
            permutation(new_list,i+1,output)
            ilist[i] = a
            ilist[j] = tmp
    else:
        print ilist

def permutation_iter(ilist):
    

test_list = [1,2,3,4]
output = []
permutation(test_list,0,output)
