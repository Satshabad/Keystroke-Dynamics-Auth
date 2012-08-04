'''
The class contains a number of method to authenticate specific users.

Author: Shiyu
'''

from smoothProfile import *
from userstore import *

VERBOSE = True
COMPENSATION = 1

class Authenticator:

    def __init__(self, name, interval):
        '''Constructs the class'''
        self.name = name
        self.profile = SmoothProfile(name, interval)
        
    def initNormalizingConst(self, validationSet):
        '''
        Get the normalizing prior for the user given a validationSet.
        The validation set is a list of inputs that the user types to get train
        his/her probability prior.
        ''' 
        sample = []
        for (event, time) in validationSet:
            if (self.profile.exists(event)) and (time < MAX_TIME):
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
        return self.const
        
    def initConstWithFullValidation(self):
        self.validationSet = User(self.name).getFullValidationSet()
        self.initNormalizingConst(self.validationSet)
        
    def getLikelihood(self, testSet):
        '''
        Get the likelihood of the user being correct.
        '''
        prob = 1.0
        for (event, time) in testSet:
            if (self.profile.exists(event)) and (time < MAX_TIME):
                prob *= COMPENSATION * self.const * self.profile.getProb(event, time)
        return prob
        
    def getLikelihoodFromProfile(self, name):
        other = User(name)
        return self.getLikelihood(other.getValidationSample(50))
        
        
if __name__ == '__main__':
    auth = Authenticator('zjlszsy', 25)
    auth.initConstWithFullValidation()
    print auth.getLikelihoodFromProfile('zjlszsy')
    print auth.getLikelihoodFromProfile('shiyu')
    print auth.getLikelihoodFromProfile('shiyu2')
    print auth.getLikelihoodFromProfile('standard')
    #print auth.getLikelihoodFromProfile('yes1')
    #print auth.getLikelihoodFromProfile('yes2')
    print '----------------------------'
    print auth.getLikelihoodFromProfile('chandra')
    print auth.getLikelihoodFromProfile('satshabad2')
    #print auth.getLikelihoodFromProfile('test_positive')
    #print auth.getLikelihoodFromProfile('allen')
    #print auth.getLikelihoodFromProfile('allen_copy')
    print auth.getLikelihoodFromProfile('channie1')
    print auth.getLikelihoodFromProfile('channie2')
    print auth.getLikelihoodFromProfile('channie3')



    #print auth.initNormalizingConst()