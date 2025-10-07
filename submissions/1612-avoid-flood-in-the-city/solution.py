class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        LENGTH = len(rains)
        ans = [-1 if r > 0 else 2 for r in rains]
        full_lakes = set()
        start = False
        startIdx = None
        dry_days = []

        for i, lake in enumerate(rains):

            if lake != 0:
                if start:
                    # first facing non-zero
                    start = False
                    if len(full_lakes) != 0:
                        dry_days.append({
                            "start": startIdx,
                            "end": i - 1,
                            "full_lakes": full_lakes.copy()
                        })
                ans[i] = -1
                if lake in full_lakes:
                    if len(dry_days) != 0:
                        found = False
                        keys_to_remove = []

                        for i, day in enumerate(dry_days):
                            if lake in day["full_lakes"]:
                                day["full_lakes"].remove(lake)

                                if not found:
                                    found = True
                                    ans[day["end"]] = lake
                                    day["end"] = day["end"] - 1
                                                                
                                if len(day["full_lakes"]) == 0 or day["start"] > day["end"]:
                                    keys_to_remove.append(i)
                        
                        if not found:
                            return []
                        else:
                            # remove keys from backward to avoid array out-of-bound
                            for k in keys_to_remove[::-1]:
                                dry_days.pop(k)

                        
                    else:
                        return []
                else:
                    full_lakes.add(lake)
            elif len(full_lakes) != 0: # facing 0

                if not start:
                    startIdx = i
                    start = True

                num_of_0 = (i - startIdx) + 1

                # optimization: if 0s we have is equal to len(full_lakes)
                # we could just try these lakes
                if num_of_0 == len(full_lakes):
                    while len(full_lakes) != 0:
                        ans[startIdx] = full_lakes.pop()
                        startIdx += 1
                    start = False

        return ans
        
