public class search_insert_position {
   public int searchInsertPos(int[] A, int target) {
        int start = 0, end = A.length-1;

        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            
            if (A[mid] == target) {
                return mid;
            } else if (A[mid] > target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        if (A[start] == target) return start;
        if (A[end] == target) return end;
        
        return end;
   } 
}
