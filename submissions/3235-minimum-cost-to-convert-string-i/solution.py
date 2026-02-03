class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def get_cost(cost_matrix, origin, changed):
            if origin in cost_matrix and changed in cost_matrix[origin]:
                return cost_matrix[origin][changed]
            return float("inf")
        def set_cost(cost_matrix, origin, changed, cost):
            if not origin in cost_matrix:
                cost_matrix[origin] = {}
            cost_matrix[origin][changed] = cost

        # using original, changed and cost to creat an orginal cost
        input_cost = {}
        chars = set()
        for i in range(len(original)):
            original_char = original[i]
            changed_char = changed[i]
            changed_cost = cost[i]

            chars.add(original_char)
            chars.add(changed_char)

            set_cost(
                input_cost,
                original_char, changed_char, 
                min(
                    get_cost(input_cost, original_char, changed_char), 
                    changed_cost
                )
            )

        # process from orginal cost to comput optimize cost
        # x1 -> x2 cost v1
        # x2 -> x3 cost v2
        # x1 -> x3 cost v3, which should be min(x1->x2+x2->x3, x1->x3)
        # which is all-pair shortest path
        # compute optimized_cost with all-pair shortest path algorithm

        optimized_cost = input_cost
        for middle in chars:
            for origin in chars:
                for changed in chars:
                    if origin != middle and changed != middle and origin != changed:
                        origin_to_changed = get_cost(optimized_cost, origin, changed)
                        origin_to_middle = get_cost(optimized_cost, origin, middle)
                        middle_to_changed = get_cost(optimized_cost, middle, changed)
                        if origin_to_changed != float("inf") or origin_to_middle + middle_to_changed != float("inf"):
                            set_cost(
                                optimized_cost, origin, changed, 
                                min(origin_to_changed, origin_to_middle + middle_to_changed)
                            )


        # iterate over source and target to compute minimun cost
        total_cost = 0
        for i in range(len(source)):
            source_char = source[i]
            target_char = target[i]
            if source_char != target_char:
                if source_char in optimized_cost and target_char in optimized_cost[source_char]:
                    total_cost += optimized_cost[source_char][target_char]
                else:
                    return -1

        return total_cost
