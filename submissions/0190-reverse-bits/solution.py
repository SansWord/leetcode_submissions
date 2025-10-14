class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for i in range(32):
            # Extract the least significant bit (LSB) of n
            lsb = (n >> i) & 1 
            
            # Shift the LSB to its reversed position (31 - i)
            # and use OR to set the corresponding bit in reversed_n
            reversed_n |= (lsb << (31 - i)) 
        return reversed_n
        
