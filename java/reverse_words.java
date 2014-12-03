public class reverse_words {
    public String reverseWords(String s) {
        StringBuilder reversed = new StringBuilder();

        int j = s.length();
        for (int i = s.length() - 1;i >= 0; i--) {
            if (s.charAt(i) == ' ') {
                j = i;
            } else if (i == 0 || s.charAt(i-1) == ' ') {
                if (reversed.length() != 0) {
                    reversed.append(' ');
                }
                reversed.append(s.substring(i,j));
            }
            
        }
        return reversed.toString();
    }

    // In-place, in which case char[] should be used instead of String, because as an object String can not be modified
    public void reverseWordsII(char[] s) {
        int len_s = s.length;
        // first reverse the entire string
        reverse(0, len_s-1, s);

        // then reverse each word in the string
        int j = -1;
        for (int i = 0; i < len_s; i++) {
            if (s[i] == ' ') {
                j = i;
            } else if (i == len_s-1 || s[i+1] == ' ') {
                reverse(j+1,i,s);
            }
        }
    }

    // reverse a string 
    public void reverse(int s, int e, char[] string) {
        char tmp;
        while (s<e){
            tmp = string[s];
            string[s] = string[e]; 
            string[e] = tmp;
            s++;
            e--;
        }
    }

    public static void main(String[] args) {
        reverse_words rw = new reverse_words();
        char[] s = "hello word".toCharArray();
        rw.reverseWordsII(s);
        System.out.println(s);
    }
}
