'''
network distribution calculate engine
'''

import numpy as np
import threading
import cyclequeue as cycle

# MAX_WORKER_NUM=8

class exector(object):
    def __init__(self, num):
        # worker thread num
        self.worker_num = num
        self.is_ok = False
        self.is_pause = True
        self.is_task_set = False

        self.running = []
        self.finished = []
        self.max_task_num = 8
        self.tasks_num = 0

        self.queue = cycle.cyclequeue(num)
        # thread manager
        self.workers = []
        self.tasks = []

        # signal for worker return
        '''
          self.signal.set()
          self.signal.clear()
          suspend is clear is call
          self.signal.wait() 
          '''
        self.signal = threading.Event()
        
        # make sure one thread send the signal in one time
        self.lock = threading.Lock()
        
    def static_list(self):
        print('[INFO] the task num in network engine is %d.'%(self.tasks_num))
        if self.is_ok == True:
            print('[INFO] the worker built in network engine is %d'%len(self.workers))
        
    # submit the cal task
    def assign_task(self, num = -1):
    
        if num <= 0:
            print('[INFO] illegal task num')
            return False
            
        if self.tasks_num == 0 or self.is_task_set == False:
            print('[INFO] please add task to network engine first, this interface is used to sumbit tasks more.')
            return False
            
        if num + self.tasks_num > self.max_task_num:
            print('[ERROR] task num is out of range %d.\n'%(self.max_task_num))
            return False
            
        else:
            for i in range(num):
                  self.tasks.append(self.tasks[0])
                  self.running.append(0)
                  self.finished.append(0) 
            self.tasks_num = self.tasks_num + num 
            print('[INFO] assign %d task in network engine.'%(num)) 
            self.static_list()
            
        return True    
        
    def add_task(self, task, num):
        
        if self.is_task_set == False:
            if num <= 0 or num > self.max_task_num or self.tasks_num:
                return False
            self.tasks_num = num

            for i in range(num):
                  self.tasks.append(task)
                  self.running.append(0)
                  self.finished.append(0)
                  
            self.is_task_set = True
            print('[INFO] network engine allow to submit tasks.')
            self.static_list()
            
        else:
            print('[INFO] task has set, please use the assgin interface to add the new one.\n')
        
        return True
                  
    def check_id(self, idx):
    
        if idx <= 0 or idx > self.tasks_num:
            print('[INFO] the check %d id is out of range'%(idx))
            return False
        if self.running[idx] ==1 or self.finished[idx] == 1:
            print('[INFO] the check %d id is running or finished'%(idx))
            return False
            
        return True
                  
    def worker(self, task):
        
        while 1:
        
            if self.is_ok == False:
                print('[INFO] %s worker is out.'%(threading.current_thread().getName()))
                self.signal.set()
                return
                
            if self.is_pause == False:
                print('[INFO] %s worker is paused.'%(threading.current_thread().getName()))
                self.signal.set()
                return
                
            pop_out = []
            pop_out.clear()
            self.queue.pop(pop_out)
            print(pop_out)
            
            if len(pop_out) == 0 :
                print('[INFO] bad item pop from task queue')
                self.signal.set()
                continue
                      
            idx = pop_out[0]
            print('idx' , idx)
            # if self.check_id(idx) == False:
                  # continue
                  
            self.running[idx] = 1
            self.finished[idx] = 0
                      
            '''      
            task_temp = self.tasks[idx]
            task_temp.setFlag(self.is_parse)
            task_temp.fit()
            '''
                      
            self.running[idx] = 0
            self.finished[idx] = 1
            
            self.signal.set()
            print('[INFO] %s worker is finished.'%(threading.current_thread().getName()))
        
    def proxy(self):
    
        if self.is_ok == False:
            print('[ERROR] exector is not ok, proxy is out.')
            return
            
        if self.is_pause == False:
            return
        
        # enable the task id, or choose random label
        task_num = self.tasks_num
        dispatch_task = []
        for i in range(task_num):
            dispatch_task.append(i)
        print('[INFO] dispath task %d is'%(len(dispatch_task)),(len(dispatch_task) == task_num))
       
        # dispatch task
        self.signal.clear() 
        self.queue.setQueueMaxNum(task_num)
        self.queue.assign(dispatch_task)

        while 1:     
                         
            # check the task status
            if task_num == 0:
                print('[ERROR] task dispatch fail, the task list is empty.')
                break
              
            sum_t = 0
            for i in range(task_num):
                sum_t = sum_t + self.finished[i]
            
            print('[INFO] begin to check the task finish flag, %d'%(sum_t))
            if sum_t == task_num:               
                print('[INFO] one dispatch tasks is finished by engine.')
                break
                
            # wait for every worker return
            print('[INFO] network engine proxy is waiting...')
            self.signal.wait()
            print('[INFO] network engine proxy get the thread return.')
            self.signal.clear()
              
        for i in range(task_num):
            self.finished[i] = 0  
        print('[INFO] clear the finish flag for tasks')
        
    def build(self):
        
        if self.tasks_num <= 0:
            print('[ERROR] task num is illegel, exector worker build fail,.\n')
            return False
        
        if self.is_ok == False:
        
            self.queue.setQueueAvaliable()
            print('[INFO] start to build %d worker'%(self.worker_num))
            
            self.is_ok=True
            print('[INFO] network engine status is', self.is_ok)
            
            for i in range(self.worker_num):
                t=threading.Thread(target=self.worker, args=(self.tasks,), name = 'worker ' + str(i))
                t.setDaemon(True)
                t.start()
                self.workers.append(t) 
                
            print('[INFO] exector worker build success.')
            self.static_list()
            
        else :
            print('[INFO] exector is start, please do not build again.\n')

    def clear(self):
        pass
    def save(self):
        pass
    def load(self):
        pass
