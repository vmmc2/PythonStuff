class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = [0] * 26
        for i in range(0, len(tasks)):
            mp[ord(tasks[i]) - ord('A')] += 1
        mp.sort()
        max_val = mp[25] - 1
        idle_slots = max_val * n
        curr = 24
        while curr >= 0:
            idle_slots -= min(mp[curr], max_val)
            curr -= 1
        if idle_slots >= 0:
            return len(tasks) + idle_slots
        return len(tasks)
        
