class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        power.sort()
        spells = []
        pre = None
        for p in power:
            if p != pre:
                spells.append([p, p])
                pre = p
            else:
                spells[-1][1] += p

        # state: casted, skip_recent, skip_old
        states = [ [[None, None], [None, None], [None, None]] for i in range(len(spells)) ]
        states[0][0] = [spells[0][1], spells[0][0]]
        states[0][1] = [0, float("-inf")]
        states[0][2] = [0, float("-inf")]
    

        state_casted   = 0
        state_skipped_recent = 1
        state_skipped_old = 2
        for i in range(1, len(spells)):
            spell = spells[i]
            power = spell[0]
            damage = spell[1]
            preState = states[i-1]

            recents = []
            old = []
            castable = []

            for state in preState:
                prePower = state[1]
                powerDiff = power - prePower
                if powerDiff > 2:
                    old.append(state)
                    castable.append(state)
                elif powerDiff == 2:
                    old.append(state)
                else:
                    recents.append(state)

            preMaxD = float("-inf")
            preMax = None
            for state in preState:
                if state[0] > preMaxD:
                    preMaxD = state[0]
                    preMax = state

            castableMaxD = float("-inf")
            castableMax = None
            for state in castable:
                if state[0] > castableMaxD:
                    castableMaxD = state[0]
                    castableMax = state
            
            recentMaxD = float("-inf")
            recentMax = None
            for state in recents:
                if state[0] > recentMaxD:
                    recentMaxD = state[0]
                    recentMax = state

            oldMaxD = float("-inf")
            oldMax = None
            for state in old:
                if state[0] > oldMaxD:
                    oldMaxD = state[0]
                    oldMax = state

            
            states[i][1] = recentMax if recentMax else oldMax

            # how to prove castable always exists
            states[i][2] = oldMax

            # how to prove castable always exists
            if castableMax:
                states[i][0] = [damage + castableMax[0], power]
            else:
                states[i][0] = preMax

        
        return max(states[-1][0][0], states[-1][1][0], states[-1][2][0])