import java.util.HashMap;

class Solution {
    public static int[] findMissingAndRepeatedValues(int[][] grid) {
        HashMap<Integer, Integer> count = new HashMap<>();

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                if (!count.containsKey(grid[i][j])) {
                    count.put(grid[i][j], 1);
                } else {
                    count.put(grid[i][j], count.get(grid[i][j]) + 1);
                }
            }
        }

        int a = 0;
        int b = 0;
        for (int i = 1; i < grid.length * grid.length + 1; i++) {
            if (count.containsKey(i) && count.get(i) == 2) {
                a = i;
            } else if (!count.containsKey(i)) {
                b = i;
            }
        }
        return new int[]{a, b};
    }

    public static void main(String[] args) {
        int[] arr = findMissingAndRepeatedValues(new int[][] { { 1,3 }, { 2,2 } } );
        for (int i : arr) {
            System.out.println(i);
        }
    }
}