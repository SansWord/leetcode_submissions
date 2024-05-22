class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if(str1.length() > str2.length()) {
            return gcdHelper(str1, str2);
        } else {
            return gcdHelper(str2, str1);
        }
        
    }

    public String gcdHelper(String longStr, String shortStr) {
        
        if (shortStr.length()==0) {
            return "";
        }
        if (longStr.equals(shortStr)) {
            return longStr;
        }

        int longLength = longStr.length();
        int shortLength = shortStr.length();

        int mostRepeat = longLength / shortLength;

        String possibleCommon = shortStr.repeat(mostRepeat);
        if (longStr.equals(possibleCommon)) {
            return shortStr;
        }

        if (longStr.startsWith(possibleCommon)) {
            return gcdHelper(shortStr, longStr.substring(possibleCommon.length()));
        } else {
            return "";
        }
    }

    
}
