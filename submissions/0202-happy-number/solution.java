import java.util.HashSet;
import java.util.Set;

/**
 * @author sansword, @date 2015/10/31 17:33
 */
public class Solution {
    public boolean isHappy(int input) {
        return isHappy(input, new HashSet<Integer>());
    }

    private boolean isHappy(int current, Set<Integer> visited) {
        if(current == 1) {
            return true;
        } else {
            if(visited.contains(current)) {
                return false;
            } else {
                visited.add(current);
                return isHappy(nextInteger(current), visited);
            }
        }
    }

    private int nextInteger(int input) {
        int result = 0;
        while(input >= 10) {
            int digit = input % 10;
            result += digit * digit;
            input = input / 10;
        }
        result += input * input;
        return result;
    }
}

