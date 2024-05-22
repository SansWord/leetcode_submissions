class Solution {
    public String mergeAlternately(String word1, String word2) {
        char[] chars1 = word1.toCharArray();  
        char[] chars2 = word2.toCharArray();

        int maxLength = Math.max(chars1.length, chars2.length);
        int minLength = Math.min(chars1.length, chars2.length);

        char[] largerChars = chars1.length > chars2.length ? chars1 : chars2;

        StringBuilder resultBuilder = new StringBuilder();

        for (int i = 0; i < minLength; i++) {
            resultBuilder.append(chars1[i]);
            resultBuilder.append(chars2[i]);
        }
        
        for (int i = minLength; i < maxLength; i++) {
            resultBuilder.append(largerChars[i]);
        }

        return resultBuilder.toString();

    }
}
