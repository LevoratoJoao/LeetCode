package CheckIfExists;

import java.util.HashSet;

public class CheckIfExists {
    public static boolean checkIfExist(int[] arr) {
        HashSet<Integer> seen = new HashSet<>();

        for (int i : arr) {
            if (seen.contains(2 * i) || (i % 2 == 0 && seen.contains(i / 2))) {
                return true;
            }
            seen.add(i);
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(checkIfExist(new int[] { 10,2,5,3 }));
    }
}