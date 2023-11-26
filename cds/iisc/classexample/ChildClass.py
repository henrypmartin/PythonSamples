'''
Created on 23-Nov-2023

@author: Henry Martin
'''
from cds.iisc.classexample.ParentClass1 import ParentClass1
from cds.iisc.classexample.ParentClass2 import ParentClass2

class ChildClass(ParentClass2, ParentClass1):
    '''
    classdocs
    '''

    def methodInAll(self):
        print('Calling from ChildClass')   
    
    #will call method from ParentClass2 as this is the 1st class in inheritance hierarchy
    def inheritedMethodCaller(self):
        self.methodInParentOnly();
    
    def __init__(self):
        '''
        Constructor
        '''
        