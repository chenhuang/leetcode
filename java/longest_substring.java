import java.util.*;

public class longest_substring {

/*
 * brutal force: O(n^2): iterative all possible substrings and identify the longest one without repeat chars 
 * the identification process: match with a-z
 * better: duplicated detection during the matching: improve with moving windows.
 * pre-process: keep a record of a-z counts
 * start from the begining and moving forward until a duplication is found.
 * move the tail pointer until the duplication is removed. keep a record of the window length.
 * */

// Think about this one, it's not very useful. 
    public int longest_substring(String s) {
        s = s.toLowerCase();

        int[] char_count = new int[256];
        for (int i = 0; i < 256; i++) {
            char_count[i] = 0;
        }

        int start = 0;
        int max_so_far = 0;
        for (int e = 0; e < s.length(); e++) {
            int char_index = (int)s.charAt(e);
            while (char_count[char_index] > 0) {
                char_count[(int)s.charAt(start)]--;
                start++;
            }
            char_count[char_index]++;
            max_so_far = Math.max(max_so_far, e-start+1);
        }

        return max_so_far;
   }

    public int ls(String s) {
       boolean[] exist = new boolean[256];
       int i = 0, maxLen = 0;
       for (int j = 0; j < s.length(); j++) {
          while (exist[s.charAt(j)]) {
             exist[s.charAt(i)] = false;
             i++;
          }
          exist[s.charAt(j)] = true;
          maxLen = Math.max(j - i + 1, maxLen);
          System.out.println(i+"\t"+j+"\t"+maxLen);
       }
       return maxLen;
    }

// Substring contains 2 or more duplicated unique characters.
    public int longest_substring_II(String s) {
        int[] char_count = new int[256];
        for (int i = 0; i < 256; i++) {
            char_count[i] = 0;
        }

        int start = 0;
        int max_so_far = 0;
        for (int e = 0; e < s.length(); e++) {
            int char_index = (int)s.charAt(e);
            while (char_count[char_index] > 1) {
                char_count[(int)s.charAt(start)]--;
                start++;
            }
            char_count[char_index]++;
            max_so_far = Math.max(max_so_far, e-start+1);
        }

        return max_so_far;
        
    }

// substring contains at most two distinct characters
    public int longest_substring_III(String s) {
        int[] char_count = new int[256];
        for (int i = 0; i < 256; i++) {
            char_count[i] = 0;
        }

        int start = 0;
        int max_so_far = 0;
        for (int e = 0; e < s.length(); e++) {
            int char_index = (int)s.charAt(e);
            while (char_count[char_index] == 0 && check_count(char_count) > 1) {
                char_count[(int)s.charAt(start)]--;
                start++;
            }
            char_count[char_index]++;
            max_so_far = Math.max(max_so_far, e-start+1);
        }

        return max_so_far;
    }

    public int check_count(int[] char_count) {
        int count = 0;
        for (int i = 0; i < char_count.length; i++) {
           if (char_count[i] > 0) {
                count++;
           }
        }

        return count;
    }

    public static void main(String[] args) {
        longest_substring ls = new longest_substring();
        System.out.println(ls.longest_substring("wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"));
        System.out.println(ls.longest_substring_II("eceba"));
        System.out.println(ls.longest_substring_III("eceba"));
//        System.out.println(ls.ls("wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"));

    }
}
