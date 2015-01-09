/* 给n个正整数，一个数target，问能否从n个数中取出若干个数，他们的和为target。
 * Brutal force: O(2^n)
 * Remove duplicates along the way: DP, state[i][j]: if numbers from 1 to i can constitue j: state[i][j] = state[i-1][j-A[i]] or state[i-1][j]. Time complexity = O(n*target) 
 * state[i][target] is the number of interest: state[i-1][target-A[i]]
 * */
public class backpack {
    public int 
}
