public class BinarySearch {
    public int binarySearch(int[] array, int target) {
        int start = 0;
        int end = array.length-1;
    
        while (start + 1 < end) {
            int mid = array[start+(end-start)/2];
            if (array[mid] > target) {
                end = mid;
            } else if (array[mid] < target) {
                start = mid;
            } else {
                return mid;
            }
        }

        if (array[start] == target) {
            return start;
        }

        if (array[end] == target) {
            return end;
        }

        return -1;
    }

    public static void main(String[] args) {
        BinarySearch s = new BinarySearch();
        int[] array = {1,2,3,3,4,5};
        int result = s.binarySearch(array,10);

        System.out.println(result);
        
    }
}
