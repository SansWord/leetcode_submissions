public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int inputLength = nums.length;
        for(int i = 0; i < inputLength; i++) {
            for(int j = i+1; j < inputLength; j++) {
                if(nums[i] + nums[j] == target) {
                    return new int[] {i+1, j+1};
                }
            }
        }
        return new int[] {0, 0};
    }
}
