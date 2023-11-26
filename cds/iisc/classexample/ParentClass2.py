'''
Created on 23-Nov-2023

@author: Nomura
'''

class ParentClass2(object):
    '''
    classdocs
    '''

    def methodInParentOnly(self):
        print('Calling methodInParentOnly from ParentClass2')   
    
    def methodInAll(self):
        print('Calling methodInAll from ParentClass2')   
    
    def __init__(self, params):
        '''
        Constructor
        '''
        