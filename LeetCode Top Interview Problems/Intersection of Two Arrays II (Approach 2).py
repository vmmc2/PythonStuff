from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Approach 2: Using two dictionaries...
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        answer = []
        for i in range(len(nums1)):
            if nums1[i] not in d1:
                d1[nums1[i]] = 1
            else:
                d1[nums1[i]] += 1
        for i in range(len(nums2)):
            if nums2[i] not in d2:
                d2[nums2[i]] = 1
            else:
                d2[nums2[i]] += 1
        for key,value in d1.items():
            if key in d2:
                final = min(value, d2[key])
                for i in range(0, final):
                    answer.append(key)
        return answer
