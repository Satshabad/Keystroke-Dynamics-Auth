import pickle
import collections
from collections import defaultdict

try:
    pickle.load(open('userdata.pkl', 'r'))
except:
    pickle.dump({}, open('userdata.pkl', 'w'))


def createUser(eventlist, userID):
    user_data = defaultdict(list)
    for event in eventlist:
        user_data[event[0]].append(event[1])
    users = pickle.load(open('userdata.pkl', 'r'))
    users[userID] = user_data
    pickle.dump(users, open('userdata.pkl', 'w'))

class User:
    def __init__(self, userID):
        users = pickle.load(open('userdata.pkl'))
        self.user_data = users[userID]

    def get(self, event, lower_bound, upper_bound):
        num_of_occurs = 0
        for time in self.user_data[event]:
            if time < upper_bound and time > lower_bound:
                num_of_occurs += 1
        return num_of_occurs/float(len(self.user_data[event]))
