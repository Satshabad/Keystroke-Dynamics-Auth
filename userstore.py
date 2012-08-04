import pickle
import collections
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
        for time in self.user_data[event]:
            if time < upper_bound and time > lower_bound:
                num_of_occurs += 1
        return num_of_occurs/float(len(self.user_data[event]))
