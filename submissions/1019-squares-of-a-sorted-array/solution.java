class Solution {
    public int[] sortedSquares(int[] nums) {
        int numsSize = nums.length;
        int lastNegativeIdx = -1;
        for(int i = 0; i < numsSize; i++) {
            int current = nums[i];
            nums[i] = current * current;
            if (current < 0) {
                lastNegativeIdx = i;
            }
        }
        
        int[] result = new int[numsSize];
        int firstNonNegativeIdx = lastNegativeIdx + 1;
        // merge sort from 0:lastNegativeIdx (reversed) and firstNonNegativeIdx:(numsSize-1)
        
        int left = lastNegativeIdx;
        int right = firstNonNegativeIdx;
        int currentIdx = 0;
        while(left >= 0 && right < numsSize) {
            int leftVal = nums[left];
            int rightVal = nums[right];
            
            if (leftVal > rightVal) {
                result[currentIdx] = rightVal;
                right++;
            } else {
                result[currentIdx] = leftVal;
                left--;
            }
            currentIdx++;
        }
        
        if (left>=0) {
            for (int i = left; i >=0; i--) {
                result[currentIdx] = nums[i];
                currentIdx++;
            }
        }
        
        if (right < numsSize) {
            for (int i = right; i < numsSize; i++) {
                result[currentIdx] = nums[i];
                currentIdx++;
            }
        }
        
        
        return result;
        
    }
}
