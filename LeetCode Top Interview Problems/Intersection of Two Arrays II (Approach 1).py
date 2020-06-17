class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Approach 1: Sort both arrays and apply two pointers -> O(n1*log(n1)) + O(n2*log(n2)) + O(min(n1,n2))
        nums1.sort()
        nums2.sort()
        answer = list()
        c1 = 0
        c2 = 0
        while c1 < len(nums1) and c2 < len(nums2):
            if nums1[c1] == nums2[c2]:
                answer.append(nums1[c1])
                c1 += 1
                c2 += 1
            elif nums1[c1] < nums2[c2]:
                c1 += 1
            else:
                c2 += 1
        return answer
