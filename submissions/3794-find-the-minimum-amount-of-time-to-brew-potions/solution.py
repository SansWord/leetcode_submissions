class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        
        cooking_time = [0 for i in range(n+1)]
        pre_schedule = [0 for i in range(n+1)]

        skill_prefix_sum = [0 for i in range(n)]


        for i in range(n):
            # hacky but work because skill_prefix_sum[-1] = 0
            skill_prefix_sum[i] =  skill_prefix_sum[i-1] + skill[i]
            cooking_time[i+1] =  mana[0] * skill[i]
            pre_schedule[i+1] = mana[0] * skill_prefix_sum[i]

        if m == 1:
            return pre_schedule[-1]

        # constraints:
        # goal: choose a proper time for [i][0], time to start cooking given potion
        # once the cooking starts, the done time is already decided.
        # 1. [i][j+1] = [i][j] + cooking_time[i][j]
        # 2. [i][j] >= [i-1][j] + cooking_time[i][j]
        # 3. [i][j] <= [i-1][j+1]
        # decide all [i][0] to meet these constraints


        
        for j in range(1, m):
            schedule     = [0 for i in range(n+1)]

            maxDiff = pre_schedule[0]
            for i in range(1, n+1):
                schedule[i] = mana[j] * skill_prefix_sum[i-1]
                diff = pre_schedule[i] - schedule[i-1]
                if diff > maxDiff:
                    maxDiff = diff

            waitTime = maxDiff

            for i in range(n+1):
                schedule[i] = schedule[i] + waitTime

            pre_schedule = schedule
                

        return schedule[-1]
