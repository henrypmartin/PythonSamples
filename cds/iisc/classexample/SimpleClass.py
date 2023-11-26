'''
Created on 22-Nov-2023

@author: Nomura
'''

class SimpleClass(object):
    '''
    classdocs
    '''
    
    def simpleClassFunction(self):
        print('This is simplest of the class function')


    def simpleFunctionWithArgs(self, name:str):
        print(f'Simple function with arg {name} and instance variable {self.instvar1}')
    
    
    def simpleFunctionWithArgAndReturn(self, name:str) -> str:
        return f'Simple function with arg {name} returned as string'
    
    def __init__(self, var1):
        '''
        Constructor
        '''
        self.instvar1=var1 