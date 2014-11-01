import java.util.*;

public class longestConsecutiveSequence {
    public int longestConsecutiveSequence(int[] num) {
        Set numbers = new HashSet();

        for (int i = 0; i < num.length; i++) {
            numbers.add(num[i]);
        }

        int max_length = 0;
        for (int i = 0; i < num.length; i++) {
            int number = num[i];
            int length = 1;
        
            for (int j = number-1;;j--) {
                if (numbers.contains(j)) {
                    length += 1;
                    numbers.remove(j);
                } else {
                    break;
                }
            }

            for (int j = number+1;;j++) {
                if (numbers.contains(j)) {
                    length += 1;
                    numbers.remove(j);
                } else {
                    break;
                }
            }

            max_length = Math.max(length, max_length);
        }

        return max_length;
    }

    public static void main(String[] args) {
        longestConsecutiveSequence s = new longestConsecutiveSequence();
        int[] array = {100,4,200,1,3,2};
        System.out.println(s.longestConsecutiveSequence(array));
    }
}
