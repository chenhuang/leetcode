public spiral_matrix {
    //
    //
    //
    // 
    private List<Integer> result;
    public int[] spiralMatrix(int[][] matrix) {
        int m = matrix.length; // row number
        int n = m > 0 ? matrix[0].length : 0; // column number
        result = new ArrayList<>();

        spiralMatrix(matrix, 0, 0, m-1, n-1);
        return result;
    }

    //
    //
    //
    public void spiralMatrix(int[][] matrix, int x1, int y1, int x2, int y2) {
        if (x1 <= x2 && y1 <= y2) {
            for (int i = y1; i <= y2; i++) {
                result.add(matrix[x1][i]);
            }
            x1 += 1;
        } else return;

        if (x1 <= x2 && y1 <= y2) {
            for (int i = x1; i <= x2; i++) {
                result.add(matrix[i][y2]);
            }
            y2 -= 1;
        } else return;

        if (x1 <= x2 && y1 <= y2) {
            for (int i = y2; i >= y1; i--) {
                result.add(matrix[x2][i]);
            }
            x2 += 1;
        } else return;

        if (x1 <= x2 && y1 <= y2) {
            for (int i = x2; i >= x1; i--) {
                result.add(matrix[i][y1]);
            }
            y1 += 1;
        } else return;

        spiralMatrix(matrix, x1+1, y1+1, x2-1, y2-1);
    }
}
