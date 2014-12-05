import java.util.*;

public class one_edit_distance {
    // DP solution?
    // edit operations: 1. replace, delete, insert
    public boolean one_edit_distance(String S, String T) {
        int i = 0;
        while (i < S.length() && i < T.length()) {
            if (S.charAt(i) == T.charAt(i)) {
                i++;
            } else {
                // delete
                if (S.substring(i+1).equals(T.substring(i))) return true;
                // repalce
                if (T.substring(i).equals(T.charAt(i)+S.substring(i+1))) return true;
                // insert
                if (T.substring(i).equals(T.charAt(i)+S.substring(i))) return true;

                return false;
            }
        }
        if (Math.abs(S.length()-T.length()) == 1) return true;
        return false;
    }

    public static void main(String[] args) {
        one_edit_distance s = new one_edit_distance();
        System.out.println(s.one_edit_distance("bcd","cd"));
    }
}
