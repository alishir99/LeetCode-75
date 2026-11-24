class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        start = end = 0
        need = Counter(t)
        best = (float('inf'), 0,0)
        win = {}
        for i in range(len(s)): 
            win[s[i]] = win.get(s[i], 0)+1
            while all(win.get(c,0)>= need[c] for c in need): 
                win[s[l]] -=1
                best = min(best, (i-l+1, l, i))
                l +=1
        l, start, end = best    
        return '' if l == float('inf') else s[start:end+1]