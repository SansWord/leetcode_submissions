class Solution {
    public int lengthOfLongestSubstring(String s) {
        if(s==null || s.isEmpty()) {
            return 0;
        }
        char[] chars = s.toCharArray();
        Map<Character, Integer> visitedChars = new HashMap();
        int maxLength = 0;
        int currentLength = 0;
        int start = 0;
        int end = 0;
        for(int i = 0; i < chars.length; i++) {
            char currentChar = chars[i];
            Integer visitedPos = visitedChars.get(currentChar);
            visitedChars.put(currentChar, i);
            if(visitedPos != null) {
                if(visitedPos >= start) {
                    currentLength = end - start + 1;
                    if(currentLength > maxLength) {
                        maxLength = currentLength;
                    }
                    start = visitedPos+1;
                }
            }
             end = i;
        }
        
        currentLength = end - start + 1;
        if(currentLength > maxLength) {
            maxLength = currentLength;
        }
        return maxLength;
        
    }
}
