class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False
        else:
            ds = {}
            dt = {}
            for i in range(0, len(s)):
                ds[s[i]] = ds.get(s[i], 0) + 1
                dt[t[i]] = dt.get(t[i], 0) + 1
            for (key, value) in ds.items():
                if key not in dt:
                    return False
                if key in dt and dt[key] != ds[key]:
                    return False
            return True
            
        
