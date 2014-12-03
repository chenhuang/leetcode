public class valid_palindrome {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length()-1;
        
        while (i < j) {
            while (isCharorDigit(s.charAt(i)) == false) {
                i++;
            }

            while (isCharorDigit(s.charAt(j)) == false) {
                j--;
            }

            if (s.charAt(i) != s.charAt(j)) {
               return false; 
            }
            i++;
            j--;
        }

        return true;
    }

    public boolean isCharorDigit(char ch) {
        if (ch >= '0' && ch <= '9') {
            return true;
        }
        if (ch >= 'A' && ch <= 'Z') {
            return true;
        }
        if (ch >= 'a' && ch <= 'z') {
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
        valid_palindrome vp = new valid_palindrome();
        System.out.println(vp.isPalindrome("acbbca"));
        System.out.println(vp.isPalindrome("acbbca1"));
        
    }
}
