class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Treating the corner cases first...
        if len(intervals) <= 1:
            return intervals
        # Treating the general cases..
        intervals.sort()
        answer = []
        curr = 0
        while curr < len(intervals):
            begin = intervals[curr][0]
            end = intervals[curr][1]
            curr += 1
            while curr < len(intervals):
                if end >= intervals[curr][0]: # Da para fazer a uniao
                    if end < intervals[curr][1]:
                        end = intervals[curr][1]
                else:
                    break
                curr += 1
            answer.append([begin, end])
        return answer
        
