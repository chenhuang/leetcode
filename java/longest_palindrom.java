/* worst case: O(n^3)
 * lots of duplications, so use DP: 
 * 1. the check of palindrom
 * lp[i][j] if string[i-j] is a palindrom:
 * lp[i][j] = lp[i+1][j-1] and s[i] == s[j]
 * Now it's O(n^2)
 *
 * 2. Can it be better? 
 *
 * */

public class longest_palindrom {


}
