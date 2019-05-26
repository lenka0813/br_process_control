import numpy as np

'''
y=apx, train for the data center and represent 
'''

class fusion_node(object):
    ''' 
    weight init: center number(trainable), the weight for transfomation
    '''
    def __init__(self, name, dim, c_num,iter, learning_rate=0.1, activate_fn='sigmod'):
        self.name=name
        self.c_num=c_num
        self.dim=dim
        self.iter=iter
        self.learning_rate=learning_rate
        self.belongs=[]

    def build(self):
        # cluster center
        self.center=np.zeros([self.dim, self.c_num])
        self.c_diff=self.center
        # cluster center bais
        self.bais=np.zeros([self.dim,1])
        self.b_diff=self.bais
        # regression weight 
        self.weight=np.zeros([self.dim,self.c_num])
        self.w_diff=self.weight
        # 
    def save(self, path, flag):
        pass

    def activate_fn(self, input, index = -1):
        n=np.shape(in)
        outs=[]
        if index > self.c_num or index < -2:
            arise 'the index of activate if out of range, or the index is illeagel'
        if index == -1:
            for i in range(self.c_num)-1:
                temp=input-self.center[i]
                out=np.exp(-np.dot(temp,temp.T)/self.bais[i])
                outs.append(out)
        else:
            temp=input-self.center[index]
            out=np.exp(-np.dot(temp,temp.T)/self.bais[index])
            outs.append(out)
        return outs
        
    '''
    forward pass
    '''
    def forward(self, input):
        nd=np.shape(input)[0]
        outs=[]
        self.belongs=[]
        for i in range(nd):
            belong=activate_fn(input)
            out=np.dot(np.dot(belongs,self.weight),input.T)
            self.belongs.append(belong)
            outs.append(out)
        return outs
    '''
    feed the input data (remain for batch)
    '''
    def feed(self, input):
        pass
    
    '''
    batch weight learning
    '''
    def backfit(self, diff, input=[]):

        nd=np.shape(input)[0]
        self.c_diff=diff[0]*activate_out*-2*(input[0]-self.center)/self.bais
        self.b_diff=diff[0]*activate_out*np.sum((x-c)*(x-c),axis=1)/self.bais
        # update weight
        self.w_diff=activate_out*input

        for i in range(1:nd):
            # update center and bais
            activate_out=activate_fn(input[i])
            self.c_diff=self.c_diff+diff[i]*activate_out*-2*(input-self.center)/self.bais
            self.b_diff=self.b_diff+diff[i]*activate_out*np.sum((x-c)*(x-c),axis=1)/self.bais
            # update weight
            self. w_diff=self.w_diff+diff[i]*activate_out*input

        # update center and bais
        self.center=self.center+self.c_diff*self.learning_rate
        self.bais=self.bais+self.b_diff*self.learning_rate

        # update weight
        self.weight=self.weight+self.w_diff*self.learning_rate
    
    def update(self, diff, input):
        #do some policy for learning rate

        # random grad selection
        if np.random.rand() > 0.4:
            return 
        # update center and bais
        activate_out=activate_fn(input)
        self.c_diff=activate_out*-2*(input-self.center)/self.bais
        self.b_diff=activate_out*np.sum((x-c)*(x-c),axis=1)/self.bais

        self.center=self.center+diff*self.c_diff*self.learning_rate
        self.bais=self.bais+diff*self.b_diff*self.learning_rate

        # update weight
        self.w_diff=activate_out*input
        self.weight=self.weight+diff*self.w_diff*self.learning_rate

        
    '''
    tranmit the node diff to previous node
    '''
    def backfit_front(self, diff):
        nd=np.shape(self.belongs)[0]
        outs=[]
        for i in range(nd):
            out=belong[i]*self.weight*diff[i]
            outs.append(out)
        retun outs

    