'''
The class contains a number of method to authenticate specific users.

Author: Shiyu
'''

VERBOSE = True

class Authenticator:

    def Authenticator(self, profile, interval):
        '''Constructs the class'''
        self.name = profile.getName()
        self.roughProfile = profile
        self.interval = interval
        self.profile = profile.getSmoothProfile(self.interval)
        
    def initNormalizingConst(self, validationSet):
        '''
        Get the normalizing prior for the user given a validationSet.
        The validation set is a list of inputs that the user types to get train
        his/her probability prior.
        ''' 
        sample = []
        for (event, time) in validationSet:
            if self.profile.hasProbDist(event):
                sample.append(self.profile.getProb(event, time))
        const = 1.0
        magnitude = 0.0 # we have magnitude so that the float doesn't overflow
        for prob in sample:
            const = const / prob
            if const > 100:
                magnitude += 2.0
                const = const / 100
        size = len(sample)
        self.const = const ** (1.0/size) * 10 ** (magnitude/size)
        
    def getLikelihood(self, testSet):
        '''
        Get the likelihood of the user being correct.
        '''
        prob = 1.0
        for (event, time) in testSet:
            if self.profile.hasProbDist(event):
                prob *= self.const * self.profile.getProb(event, time)
                if VERBOSE:
                    print "Event=", event, "; Time=", time, "; Prob=", prob
        return prob