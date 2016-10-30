import java.util.*;
import java.util.stream.Collectors;

public class Solution {
    public int firstUniqChar(String s) {
        if (s == null) {
            return -1;
        } else {
            int strLen = s.length();
            if (strLen == 0) {
                return -1;
            } else {
                return fastSolution(s);
            }
        }
    }

    private int fastSolution(String s) {
        int strLen = s.length();
        Map<Character, Integer> firstShown = new HashMap<>();
        List<Integer> candidates = new ArrayList<>();
        Set<Character> shown = new HashSet<>();
        for (int i = 0; i < strLen; i++) {
            char currentChar = s.charAt(i);
            if (shown.contains(currentChar)) {
                Integer first = firstShown.get(currentChar);
                if (first != null) {
                    int index = candidates.indexOf(first);
                    candidates.remove(index);
                    firstShown.remove(currentChar);
                }
            } else {
                shown.add(currentChar);
                firstShown.put(currentChar, i);
                candidates.add(i);
            }
        }

        if (candidates.size() != 0) {
            return candidates.get(0);
        } else {
            return -1;
        }
    }
}
