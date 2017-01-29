public class Solution {
    public int reverse(int x) {
        boolean isMinus = 0L > x;
        if (isMinus) {
            x = Math.abs(x);
            if(0L > x) {
                return 0;
            }
        }
        char[] newChars = reverseCharArray(String.valueOf(x).toCharArray());
        Long l = Long.parseLong((isMinus ? "-" : "") + String.valueOf(newChars));
        if(l > Integer.MAX_VALUE || l < Integer.MIN_VALUE) {
            return 0;
        } else {
            return l.intValue();
        }
    }

    private char[] reverseCharArray(char[] chars) {
        char[] newChars = new char[chars.length];
        for (int i = 0; i < chars.length; i++) {
            newChars[i] = chars[chars.length - 1 - i];
        }
        return newChars;
    }
}
