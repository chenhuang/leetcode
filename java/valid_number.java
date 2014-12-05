public class valid_number {
// exponential numbers are invalid
/* A couple of things to consider: 
 * 1. trailing and ending spaces.
 * 2. +/- symbols
 * 3. decimal points
 * */
    public boolean isNumber(String s) {
        int start = 0, end = s.length()-1;

        // determine the start and end of a string s
        while (start <= end && Character.isWhitespace(s.charAt(start))) start++;
        while (start <= end && Character.isWhitespace(s.charAt(end))) end--;

        // detect if there is any +/- symbol
        if (start <= end && (s.charAt(start) == '+' || s.charAt(start) == '-')) start++;

        // detect content of the number string
        int decimal_count = 0;
        int e_count = 0; 
        boolean isValid = false;
        while (start <= end) {
            if (Character.isDigit(s.charAt(start))) {
                isValid = true;
            } else if (s.charAt(start) == '.' && decimal_count < 1) {
                if (e_count > 0) return false;
                decimal_count++;
            } else if (isValid && s.charAt(start) == 'e' && e_count < 1) {
                e_count++;
                start++;
                isValid = false;
                if (start <= end && (s.charAt(start) == '+' || s.charAt(start) == '-')) start++;
                while (start <= end) {
                    if (Character.isDigit(s.charAt(start))) {
                        isValid = true;
                    } else {
                        return false;
                    }
                    start++;
                }
                return isValid;
            } else {
                return false;
            }
            start++;
        }
        return isValid;
    }

    public static void main(String[] args) {
        valid_number vn = new valid_number();
        System.out.println(vn.isNumber("e"));
    }
}

