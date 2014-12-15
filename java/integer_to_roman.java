public class integer_to_roman {
    // since the range is 1-3999: I to MMMDCCCCLXXXXVV
    // divide by 1000
    // divide by 500
    // divide by 100
    private static final int[] values = {
        1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1

    };  

    private static final String[] symbols = {
        "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
    };

    public String integer2Roman(int num) {
        StringBuilder roman = new StringBuilder();
        int i = 0;
        while (num > 0) {
            int k = num / values[i];
            for (int j = 0; j < k; j++) {
                roman.append(symbols[i]);
                num -= values[i];
            }
            i++;
        }
        return roman.toString();
    }
}
