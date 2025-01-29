class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        while (i < j) {
            Character left = s.charAt(i);
            Character right = s.charAt(j);
            if (!Character.isLetterOrDigit(left)) {
                i += 1;
            } else if (!Character.isLetterOrDigit(right)) {
                j -= 1;
            } else {
                if (Character.toLowerCase(right) != Character.toLowerCase(left)) {
                    return false;
                }
                i += 1;
                j -= 1;
            }
        }
        return true;
    }
}