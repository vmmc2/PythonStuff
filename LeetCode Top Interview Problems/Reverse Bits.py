class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        for i in range(0, 32):
            carry = n & 1
            answer = answer | carry
            n = n >> 1
            if i == 31:
                break
            answer = answer << 1
        return answer
