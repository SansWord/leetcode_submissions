class Solution:
    def minimumDeletions(self, s: str) -> int:
        # delete all 'b's before the last 'a'
        # or delete 'a'
        result = 0
        a_count = 0
        b_count = 0
        for c in s:
            if c == 'a':
                a_count += 1
            else:
                b_count += 1

        # if there's only a or b in the string, it's already valid and does not have to remove anything
        if a_count == 0 or b_count == 0:
            return 0
        
        curr_a = 0
        curr_b = 0
        # most easy way is to remove all a from the string, and let's find the optimal from this
        min_removals = min(a_count, b_count)

        for i, c in enumerate(s):
            if c == 'a':
                # threat this 'a' as the last 'a' of final string
                # remove all b before i and all a after this a
                curr_a += 1
                a_count_after = a_count - curr_a
                b_count_before = i + 1 - curr_a

                curr_removals = a_count_after + b_count_before
                min_removals = min(min_removals, curr_removals)
        
        return min_removals

                

        
