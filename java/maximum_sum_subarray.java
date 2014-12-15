public class maximum_sum_subarray {
    public int maxSubArray(int[] input) {
       // pre-process input array:
       int[] sum_so_far = new int[input.length];
       sum_so_far[0] = input[0];

       for (int i = 1; i < input.length; i++) {
            sum_so_far[i] = sum_so_far[i-1] + input[i];
       }

       // now compute the max difference between two points:
       int max_so_far = 0;
       int min = sum_so_far[0];
       for (int i = 0; i < sum_so_far.length; i++) {
            if (sum_so_far[i] < min) { 
                min = sum_so_far[i];
            } else {
                max_so_far = Math.max(max_so_far, sum_so_far[i]-min);
            }
       } 

        return max_so_far;
    }
}
