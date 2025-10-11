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
        
        self.spells = spells
        self.spellsLen = len(spells)
        self.mem = [-1 for i in range(self.spellsLen)]
        for i in range(self.spellsLen, 0, -1):
            self.findMaxDamage(i)

        return self.findMaxDamage(0)

    def findMaxDamage(self, idx:int) -> int:
        if idx >= self.spellsLen:
            return 0

        if self.mem[idx] != -1:
            return self.mem[idx]
        
        skippedDamageIdx = idx+1

        castDamage = self.spells[idx][1]
        spellPower = self.spells[idx][0]

        found = False
        foundIdx = None

        for i in range(idx+1, self.spellsLen):
            power = self.spells[i][0]
            if power > spellPower+2:
                found = True
                foundIdx = i
                break

        if found:
            if skippedDamageIdx == foundIdx:
                damage = castDamage + self.findMaxDamage(foundIdx)
            else:
                damage = max(castDamage + self.findMaxDamage(foundIdx), self.findMaxDamage(skippedDamageIdx))
        else:
            damage = max(self.findMaxDamage(skippedDamageIdx), castDamage)

        self.mem[idx] = damage
        return damage


