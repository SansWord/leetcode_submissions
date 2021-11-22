/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        //System.out.println("---------:" + n);
        return binaryFind(1, n);
    }
    
    private int binaryFind(int left, int right) {
        if(left>right) {
            //System.out.println("----left:" + left +", right:" + right);
            return left + (isBadVersion(left) ? 0 : 1);
        }
        int current = left + (right-left)/2;
        //System.out.println("----left:" + left +", right:" + right + ", current:" + current);
        if(isBadVersion(current)) {
            return binaryFind(left, current-1);
        } else {
            return binaryFind(current+1, right);
        }
    }
}
