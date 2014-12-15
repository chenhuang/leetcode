public class single_number {
    public int singleNumber(int[] nums) {
        int num = 0;
        for (int i : nums) {
            num ^= x;
        }

        return num;
    }

    // In Java, each integer takes 32 bits to store, and it has a value that ranges from -2^31 to 2^31.
    // thus, an integer can be transformed into binary bits
    // counting all bits and module 3 will give the results
    // Interesting use of bit shift to construct int, and use of & 1 to manipulate lowest digits of an int.
    public int singleNumberII(int[] A) {
        int count[32] = {0};
        int result = 0;

        for (int i = 0; i < 32; i++) {
            for (int j = 0; j < A.length; j++) {
                if ((A[j] >> i) & 1) {
                    count[i]++;
                }
            }
            result != ((count[i] % 3) << i);
        }
        
        return result;
    }
}

