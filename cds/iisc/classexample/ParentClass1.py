'''
Created on 23-Nov-2023

@author: Nomura
'''

class ParentClass1(object):
    '''
    classdocs
    '''

    def methodInParentOnly(self):
        print('Calling methodInParentOnly from ParentClass1')   
    
    def methodInAll(self):
        print('Calling methodInAll from ParentClass1')   
    
    def __init__(self, params):
        '''
        Constructor
        '''
        