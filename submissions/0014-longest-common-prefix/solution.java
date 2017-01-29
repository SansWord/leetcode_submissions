public class Solution {
    public String longestCommonPrefix(String[] strs) {
        int num = strs.length;
        if (num == 0) {
            return "";
        }
        if (num == 1) {
            return strs[0];
        }
        char[][] charsArr = new char[num][];

        for (int i = 0; i < strs.length; i++) {
            charsArr[i] = strs[i].toCharArray();
        }
        int j = 0;
        boolean looping = true;
        while (looping) {
            if (charsArr[0].length < j + 1) {
                break;
            } else {
                char match = charsArr[0][j];
                for (int i = 1; i < num; i++) {
                    if (charsArr[i].length < j + 1) {
                        looping = false;
                        break;
                    } else {
                        if (charsArr[i][j] != match) {
                            looping = false;
                            break;
                        }
                    }
                }
                if (looping) {
                    j++;
                }
            }
        }
        if (j == 0) {
            return "";
        } else {
            return strs[0].substring(0, j);
        }
    }
}
