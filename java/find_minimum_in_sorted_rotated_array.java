// 4 5 6 7 0 1 2
// start, end, mid: 
// min is the smallest number in the array: 
// A[i] < A[i-1] and A[i] < A[i+1]
// cases: 
// -----__: 
// 1. A[mid] > A[start] and A[mid] > A[end]: pivot on the right
// start = mid + 1
// --_____:
// 2. A[mid] < A[start] and A[mid] > A[end]: pivot on the left
// end = mid - 1
// 3. pivot is on mid: A[mid] < A[start] and A[mid] < A[end]
// 4. pivot is on start or end, will never be found out in the loop.
//

public class find_minimum_in_sorted_rotated_array {
    // This is not the right way to do that, too many corner cases to consider:
    public int findMin(int[] A) {
        assert(A.length > 0);

        int start = 0, end = A.length - 1;
        while (start < end && A[start] >= A[end]) {
            int mid = start + (end - start) / 2;
            if (A[mid] > A[end]) 
                start = mid + 1;
            else 
                end = mid;
        
        return A[start];
    }

    // When there are duplicates, say 1 0 1 1 1 1 or 1 1 1 1 1 0 1 1
    // , the key to identify rotation: 
    // when A[start] >= A[end] still works, but the pivot is hard to find in this case:
    // 4 5 6 7 0 1 2: 
    public int findMinII(int[] A) {
        int start = 0, end = A.length - 1;
        while (start < end && A[start] >= A[end]) {
            int mid = start + (end - start) / 2;
            if (A[mid] > A[end]) {
                start = mid+1;
            } else if (A[start] < A[end]) {
                end = mid;
            } else {
                start++;
            } 
        }

        return A[start];
    }
    
}
