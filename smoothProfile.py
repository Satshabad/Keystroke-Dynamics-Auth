'''
The class gives a smooth distribution for a specific user.

Author: Shiyu
'''

import pickle
from userstore import User

MAX_TIME = 300
MIN_EVENTS = 3
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class SmoothProfile:
    
    def __init__(self, name, interval):
        self.user = User(name)
        self.interval = interval
        self.exist = {}
        self.smooth = {}
        for char1 in UPPER_LETTERS:
            for char2 in UPPER_LETTERS:
                event = char1 + char2
                self.exist[event] = False
                self.smooth[event] = [0] * (MAX_TIME / interval)
                if (self.user.getNumEvents(event) >= MIN_EVENTS):
                    for i in range(MAX_TIME / interval):
                        self.smooth[event][i] = self.user.get(event, i*interval, (i+1)*interval)
                    self.exist[event] = True
        for char1 in UPPER_LETTERS:
            for char2 in UPPER_LETTERS:
                event = char1 + char2
                if self.exist[event]:
                    score = [0] * (MAX_TIME / interval)
                    for i in range(MAX_TIME / interval):
                        score[i] = self._getScore(i, self.smooth[event])
                    self.smooth[event] = self._normalize(score)
                #print event, self.smooth[event]
                
    def exists(self, event):
        if event[0] in UPPER_LETTERS and event[1] in UPPER_LETTERS:
            return self.exist[event]
        else:
            return False
        
    def getProb(self, event, time):
        slot = int(time / self.interval)
        return self.smooth[event][slot]
                        
    def _getScore(self, i, prob):
        score = 0.0
        for j in range(MAX_TIME / self.interval):
            if i == j:
                score += prob[j] * 10.0
            else:
                score += prob[j] / abs(i-j)
        return score
                
    def _normalize(self, score):
        result = score[:]
        s = sum(score)
        for i in range(len(score)):
            result[i] = score[i] / s
        return result
            
if __name__ == '__main__':
    a = SmoothProfile('zjlszsy', 20)