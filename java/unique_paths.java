public class unique_paths {
    public int uniquePaths(int m, int n) {
    // from (0, 0) to (m-1, n-1)
        int[][] steps = new int[m][n];
    
        for (int i = 0; i < n; i++) steps[0][i] = 1;
        for (int i = 0; i < m; i++) steps[i][0] = 1;

        for (int i = 1; i < m; i++) 
            for (int j = 1; j < n; j++) {
                steps[i][j] = steps[i][j-1] + steps[i-1][j];
            }

        return steps[m-1][n-1];
    }

    public in uniquePathsII(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;

        int steps = new int[m][n];

        boolean isBlocked = false;
        for (int i = 0; i < m; i++) 
            if (obstacleGrid[i][0] == 0 && isBlocked == false)
                steps[i][0] = 1;
            else {
                steps[i][0] = 0;
                isBlocked = true;
            }

        isBlocked = false;
        for (int i = 0; i < n; i++) 
            if (obstacleGrid[0][i] == 0 && isBlocked == false)
                steps[0][i] = 1;
            else {
                steps[0][i] = 0;
                isBlocked = true;
            }

        for (int i = 1; i < m-1; i++) {
            for (int j = 1; j < n-1; j++) {
                steps[i][j] = steps[i][j-1] + steps[i-1][j];
                if (obstacleGrid[i][j] == 1) {
                    steps[i][j] = 0;
                }
            }
        }

        return steps[m-1][n-1];
    }
}

