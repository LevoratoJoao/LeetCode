class Solution {
    public static int maxRepeating(String sequence, String word) {
        int count = 0;
        while (sequence.contains(word.repeat(count))) {
            count += 1;
        }
        return count - 1;

    }

    public static void main(String[] args) {
        System.out.println(maxRepeating("aaabaaaabaaabaaaabaaaabaaaabaaaaba"
, "aaaba"));
    }
}

