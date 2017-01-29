public class Solution {
    public boolean circularArrayLoop(int[] nums) {
        int size = nums.length;
        Boolean[] nodeVisited = new Boolean[size];
        Boolean[] loopChecked = new Boolean[size];
        Arrays.fill(nodeVisited, false);
        Arrays.fill(loopChecked, false);
        int start = 0;
        while (!allVisited(nodeVisited)) {
            int loopStart = findLoopStart(nums, nodeVisited, start);
            if(!loopChecked[loopStart]) {
                loopChecked[loopStart] = true;
                if(isLoop(nums, loopStart)) {
                    return true;
                }
            }
            start = nextUnvisited(nodeVisited);
        }

        return false;
    }

    private int nextUnvisited(Boolean[] visited) {
        for (int i = 0; i < visited.length - 1; i++) {
            if (!visited[i]) {
                return i;
            }
        }
        return -1;
    }

    private boolean allVisited(Boolean[] visited) {
        for (int i = 0; i < visited.length - 1; i++) {
            if (!visited[i]) {
                return false;
            }
        }
        return true;
    }

    private int findLoopStart(int[] nums, Boolean[] visited, int start) {
        int size = nums.length;
        int current = start;
        while (!visited[current]) {
            visited[current] = true;
            int step = nums[current];
            current = getNextStep(size, current, step);
        }
        return current;
    }

    private boolean isLoop(int[] nums, int start) {
        int size = nums.length;
        int next = -1;
        int current = start;
        int length = 0;
        boolean sameDirection = true;
        boolean flag = nums[current] < 0;
        while (next != start) {
            int step = nums[current];
            if (step < 0 != flag) {
                sameDirection = false;
            }
            length++;
            next = getNextStep(size, current, step);
            current = next;
        }

        return length >= 2 && sameDirection;
    }

    private int getNextStep(int size, int current, int step) {
        return (((current + step) % size) + size) % size;
    }
}
