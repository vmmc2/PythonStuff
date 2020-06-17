class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse() # lists sao mutaveis, nao preciso criar uma nova lista ao modifica-la.
        carry = 1
        for i in range(0, len(digits)):
            if digits[i] + carry <= 9:
                digits[i] = digits[i] + carry
                carry = 0
            else:
                carry = 1
                digits[i] = (digits[i] + carry) % 10
            if carry == 0:
                break
        if carry == 1:
            digits.append(1)
        digits.reverse()
        return digits
        
        
