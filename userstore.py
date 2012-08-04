import pickle
import collections
import random
from collections import defaultdict



def createUser(userID, eventlist):
    try:
        user_data = pickle.load(open(userID+'.data', 'r'))
    except:
        user_data = defaultdict(list)
        print 'this should not appear'
    for event in eventlist:
        user_data[event[0]].append(event[1])
        print event[0]
    pickle.dump(user_data, open(userID+'.data', 'w'))

class User:
    def __init__(self, userID):
        self.user_data = pickle.load(open(userID+'.data'))

    def get(self, event, lower_bound, upper_bound):
        num_of_occurs = 0
        if event not in self.user_data.keys():
            raise ValueError("No such events!")
        for time in self.user_data[event]:
            if time < upper_bound and time > lower_bound:
                num_of_occurs += 1
        return num_of_occurs/float(len(self.user_data[event]))
        
    def getNumEvents(self, event):
        return len(self.user_data[event])
        
    def getFullValidationSet(self):
        lst = []
        for event in self.user_data:
            for time in self.user_data[event]:
                lst.append((event, time))
        return lst

    def getValidationSample(self, num):
        lst = self.getFullValidationSet()
        sample = []
        for i in range(num):
            sample.append(random.choice(lst))
        return sample