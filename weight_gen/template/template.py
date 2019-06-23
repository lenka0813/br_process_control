import numpy as np

'''
y=apx, train for the data center and represent 
'''

class fusion_node(object):
    ''' 
    weight init: center number(trainable), the weight for transfomation
    '''
    def __init__(self, name, c_num,activate_fn='sigmod'):
        self.name=name
        self.c_num=c_num

    def build(self):
        
    '''
    forward pass
    '''
    def forward(self):
        pass
    '''
    feed the input data
    '''
    def feed(self,input):
        pass
    
    '''
    weight learning
    '''
    def backfit(self,diff):
        pass
    
    def update(self):
        pass
    '''
    tranmit the node diff to previous node
    '''
    def backfit_front(self):
        pass
    