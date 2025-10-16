class Solution:
    def maximum69Number (self, num: int) -> int:
        # change the first 6 into 9.
        res = []
        found = False
        for c in str(num):
            if not found and c == "6":
                found = True
                res.append("9")
            else:
                res.append(c)

        return int("".join(res))
