import java.util.*;

/**
 * @author sansword, @date 2015/10/31 下午 5:33
 */
public class Solution {

    private static final String ARROW = "->";

    public List<String> binaryTreePaths(TreeNode root) {
        return generateOutput(binaryTreePathsHelper(root));
    }

    public List<List<Integer>> binaryTreePathsHelper(TreeNode processingNode) {
        if (processingNode == null) {
            return Collections.emptyList();
        } else {
            // FIXME if there are two empty child, there'll be two current path, which is not correct.
            List<List<Integer>> leftPaths = binaryTreePathsHelper(processingNode.left);
            List<List<Integer>> rightPaths = binaryTreePathsHelper(processingNode.right);
            List<List<Integer>> result = new ArrayList<List<Integer>>(leftPaths.size() + rightPaths.size());
            result.addAll(leftPaths);
            result.addAll(rightPaths);
            return prependToPaths(result, processingNode.val);
        }

    }

    public static List<List<Integer>> prependToPaths(List<List<Integer>> paths, final int input) {
        if (paths.isEmpty()) {
            List<Integer> firstList = new ArrayList<Integer>();
            firstList.add(input);
            return Collections.singletonList(firstList);
        } else {
            for (List<Integer> path : paths) {
                path.add(0, input);
            }
            return paths;
        }
    }

    static private String joinPath(List<Integer> path) {
        StringBuilder result = new StringBuilder();
        if (path.size() > 0) {
            result.append(path.get(0));
            for (int i = 1; i < path.size(); i++) {
                result.append(ARROW);
                result.append(path.get(i));
            }
        }

        return result.toString();
    }

    public List<String> generateOutput(List<List<Integer>> integerPaths) {

        List<String> result = new ArrayList<String>(integerPaths.size());

        for (List<Integer> integerPath : integerPaths) {
            result.add(joinPath(integerPath));
        }

        return result;
    }
}



