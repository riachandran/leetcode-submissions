class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textf = defaultdict(int)
        word = defaultdict(int)
        
        for t in text:
            if t in 'balloon':
                textf[t] += 1
        
        for ch in 'balloon':
            word[ch] += 1
            
        for ch in textf:
            textf[ch] = int(textf[ch]/word[ch])

            
        if len(textf) == 5:
            return min(textf.values())
        else:
            return 0
