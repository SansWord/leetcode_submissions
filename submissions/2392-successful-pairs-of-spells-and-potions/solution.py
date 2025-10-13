class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)

        result = [0] * n
        spells_pos = defaultdict(list)
        potions_count = defaultdict(int)

        for i in range(n):
            spells_pos[spells[i]].append(i)
        
        for i in range(m):
            potions_count[potions[i]] += 1

        spells_strength = sorted(list(spells_pos.keys()), reverse=True)
        potions_strength = sorted(list(potions_count.keys()))

        potions_len = len(potions_strength)

        potion_counts_sums = [0] * potions_len
        potion_counts_sums[-1] = potions_count[potions_strength[-1]]
        for i in range(potions_len-2, -1, -1):
            potion_counts_sums[i] = potion_counts_sums[i+1] + potions_count[potions_strength[i]]


        # spell strength is sorted decending, means target potion strength would be increasing
        # remember and starts from previous found index would make the search faster
        # also skip all searches when spell strength is too small.
        potion_idx_min = 0
        for sp in spells_strength:
            potion_strength_minimum = ceil(success/sp)
            potion_idx = self.find_lower(potions_strength, potion_strength_minimum, potion_idx_min, potions_len)

            if potion_idx != -1:
                potion_idx_min = potion_idx
                total_potions = potion_counts_sums[potion_idx]
                
                spells_idx = spells_pos[sp]
                for idx in spells_idx:
                    result[idx] = total_potions
        
    


        return result
    
    def find_lower(self, nums: list[int], target: int, lo:int, hi:int) -> int:
        result = -1
        while lo < hi:
            mid = (lo+hi)//2
            val = nums[mid]
            if val >= target:
                result = mid
                hi = mid
            else:
                lo = mid + 1
        return result
        
