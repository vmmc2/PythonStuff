class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Solving for the corner cases first:
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        # Now solving for the general case...
        answer = []
        intervals.sort()
        cursor = 0
        while cursor < len(intervals):
            begin = intervals[cursor][0] 
            end = intervals[cursor][1]
            nxt = cursor + 1
            while nxt < len(intervals):
                if end >= intervals[nxt][0]:
                    if intervals[nxt][1] > end:
                        end = intervals[nxt][1]
                else:
                    break
                nxt += 1
            cursor = nxt
            answer.append([begin, end])
            #if cursor == len(intervals) - 1:
            #    brea
        return answer
