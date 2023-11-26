'''
Created on 22-Nov-2023

@author: Henry Martin
'''
from cds.iisc.classexample.SimpleClass import SimpleClass

sc = SimpleClass('samplevar1')

sc.simpleClassFunction()

sc.simpleFunctionWithArgs("henry")

returned_value = sc.simpleFunctionWithArgAndReturn("martin")

print(returned_value)