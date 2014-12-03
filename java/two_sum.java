import java.util.map.*;

public class two_sum {
    public int[] twoSum(int[] numbers, int target) {
        Map<Integer, Integer> record = new HashMap<Integer, Integer>();
        for (int i = 0; i < numbers.length; i++) {
            if (record.containsKey(numbers[i])) {
                return new int[] {record.get(numbers[i]),i};
            } else {
                record.put(target-numbers[i], i);
            }
        }

        throw new IllegalArgumentException("No tow sum solution");
    }

}
