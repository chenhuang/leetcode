public class maximum_product_subarray {
    // This is a careless thought, 
    // however, i was not able to identify the leak...
    public int maxProductSubarray(int[] input) {
        int max_so_far = input[0];
        int max_ending_here = input[0];

        for (int i = 1; i < input.length; i++) {
            if (max_ending_here == 0) {
                max_ending_here = input[i];
            } else {
                max_ending_here = max_ending_here * input[i];
            }

            max_so_far = Math.max(max_so_far, max_ending_here);
        }

        return max_so_far;
    }

    public int maxProduct(int[] A){
        int max_ending_here = A[0] > 0 ? A[0] : 0;
        int min_ending_here = A[0] < 0 ? A[0] : 0;
        int max_so_far = A[0];

        for (int i = 1; i < A.length; i++) {
            if (A[i] > 0) {
                max_ending_here = Math.max(max_ending_here * A[i], A[i]);
                min_ending_here = min_ending_here * A[i];
            } else if (A[i] < 0) {
                int prev_max = max_ending_here;
                max_ending_here = min_ending_here * A[i];
                min_ending_here = Math.min(prev_max * A[i], A[i]);
            } else {
                max_ending_here = 0;
                min_ending_here = 0;
            }

            max_so_far = Math.max(max_so_far, max_ending_here);
        }

        return max_so_far;
    }
    
    public int maxProduct(int[] A) {
        assert A.length > 0;
        int max = A[0], min = A[0], maxAns = A[0]; 
        for (int i = 1; i < A.length; i++) {
            int mx = max, mn = min;
            max = Math.max(Math.max(A[i], mx * A[i]), mn * A[i]);
            min = Math.min(Math.min(A[i], mx * A[i]), mn * A[i]);
            maxAns = Math.max(max, maxAns);
        }
        return maxAns;
    }
}
