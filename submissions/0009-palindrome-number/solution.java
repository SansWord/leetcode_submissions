public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        } else {
            if (x < 10) {
                return true;
            } else {
                int digitLength = getLength(x);
                for (int i = 0; i < digitLength / 2 + 1; i++) {
                    if (getFirstNthDigit(x, i) != getLastNthDigit(x, digitLength, i)) {
                        return false;
                    }
                }
                return true;
            }
        }
    }

    private int getLength(int x) {
        int length = 1;
        long stage = 10;
        while (stage <= x) {
            length++;
            stage *= 10;
        }
        return length;
    }

    // n start from 0 to digitLength
    private int getFirstNthDigit(int x, int n) {
        return (int) ((x / Math.pow(10, n)) % 10);
    }

    private int getLastNthDigit(int x, int digitLength, int n) {
        return getFirstNthDigit(x, digitLength - n - 1);
    }

    public static void main(String[] args) {
        System.out.println(new Solution().getLength(10));
        System.out.println(new Solution().isPalindrome(10));
    }
}
