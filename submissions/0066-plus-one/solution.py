class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        LENGTH = len(digits)
        carry = 0
        for i in range(LENGTH):
            idx = LENGTH - 1 - i
            d = digits[idx]
            curr = d + 1
            digits[idx] = curr % 10
            carry = curr // 10
            if carry == 0:
                return digits
        
        if carry == 1:
            digits.insert(0, 1)
        return digits

