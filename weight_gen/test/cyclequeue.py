'''
keep the queue visit security
'''

import threading

class cyclequeue(object):

    def __init__(self, max_queue=8):
        self.is_ok = False
        
        # id list for worker threads
        self.queue = []
        self.max_queue = max_queue
        '''
        thread lock
        self.lock.acquire()
        TODO:
        self.lock.release()
        '''
        self.lock = threading.Lock()

        '''
        signal if the data in queue is avaliable
        singal one or all
        
        self.event.set()
        self.event.clear()
        suspend is clear is call
        self.event.wait() 
        '''
        self.event = threading.Event()
        
    def __del__(self):
    
        self.event.set()
        self.lock.release()
        
    def setQueueAvaliable(self):
        self.lock.acquire()
        self.is_ok = True
        print('[INFO] the queue status is ok')
        self.lock.release()
        
    def setQueueUnavaliable(self):
    
        self.lock.acquire()
        self.is_ok = False
        print('[INFO] the queue status is disable')
        self.lock.release()
        
    def setQueueMaxNum(self, num):
    
        self.lock.acquire()
        if  self.is_ok == False:
            self.lock.release()
            return False
            
        self.max_queue = num
        print('[INFO] set the QueueMaxNum is %d.'%(num))
        self.lock.release()
        return True
        
    def assign(self, tasks):
    
        self.lock.acquire()
        if  self.is_ok == False:
            print('[INFO] the cycle queue is not ready !')
            self.lock.release()
            return False
            
        if (len(self.queue) + len(tasks)) > self.max_queue:
            skip_num =  len(tasks) + len(self.queue) -self.max_queue
            insert_num = self.max_queue - len(self.queue)
            self.queue = self.queue + tasks[0:insert_num]
            print('[INFO] task queue is full, %d elem is skip'%( skip_num ))
        else:
            self.queue = self.queue + tasks
            
        self.event.set()
        self.lock.release()
        return True
            
    def clear(self):
    
        self.lock.acquire()
        if  self.is_ok == False:
            self.lock.release()
            return False
        
        self.queue.clear()
        self.event.clear()
        print('[INFO] clear the queue list')
        self.lock.release()
        return True
    
    def static_list(self):
    
        self.lock.acquire()
        if  self.is_ok == False:
            self.lock.release()
            return False
        print('[INFO] the queue length is %d'%(len(self.queue)))
        self.lock.release()
        return True

    def push(self, task):
    
        self.lock.acquire()
        
        if  self.is_ok == False  :
            print('[INFO] the cycle queue is not ready !')
            self.lock.release()
            return False
        
        if len(task) > 1:
            print('[INFO] one task is allowed by push action, please use assign to add more task.')
            self.lock.release()
            return False
        
        if len(self.queue) > self.max_queue :
            print('[INFO] task queue is full, push will be skip.')
            self.lock.release()
            return False
        
        self.queue.append(task)
        self.event.set()
        print('[INFO] push one task to queue.')
        self.lock.release()
        return True        

    def pop(self, out = None):
    
        self.lock.acquire()
        if  self.is_ok == False :
            print('[INFO] the cycle queue is not ready !')
            self.lock.release()
            return False
                  
        if  len(self.queue) == 0:
            self.lock.release()
            # wait the queue avaiable signal
            print('[INFO] the queue is empty, please wait...')
            self.event.clear()
            self.event.wait()
            # regain the lock control
            self.lock.acquire()
            # self.queue.pop()
            # self.lock.release()
            # return True
        
        if out is not None:   
            if len(self.queue) > 0:
                out.append(self.queue.pop())
                print('[INFO] one queue item pop success.')
            
        self.lock.release()
        return True
        
