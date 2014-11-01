#! /usr/bin/env
# Compute power(x,n)
# x^n = (x^n/2)^2

def power(x,n):
    if n%2 == 1:
        return x*power_rec(x,n-1)
    

def power_rec(x,n):
    if n == 1:
        return x    
    else:
        left = power_rec(x,n/2) 
        return left * left

if __name__ == "__main__":
    print power(10,3)
    
