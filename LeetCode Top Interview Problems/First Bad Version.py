# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        low = 1
        high = n
        answer = n + 1
        while low <= high:
            mid = low + (high - low)//2
            if isBadVersion(mid) == True:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer
        """
        :type n: int
        :rtype: int
        """
        
