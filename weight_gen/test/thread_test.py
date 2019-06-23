import threading
import time

class test(object):
    def __init__(self, name, num):
        self.name=name
        self.num=num
    def test_print(self):
        for i in range(self.num):
            print('%s is running'%(self.name))
            time.sleep(2)
            test.print_test(self,self.num)
    def print_test(self, num):
        pass
    '''
    def timestatic(func):
        def static(name):
            start=time.time()
            func(name)
            end=time.time()
            print(func.__name__+'\'s time consume is '+str(end-start)+'ms')
        return static
    '''
    
    def pass_addr(self, p):
        p[2]=-1
        print('p is modified....')
        
    #@timestatic
    def worker(self, name):
        for i in range(3):
            print('thread'+ name +' is running.\n')
            time.sleep(1)
        print('thread'+ name +' is exit\n')
        
    @staticmethod
    def SharePtr():
        print('this is a static meathd')

threads=[]
b=test('thread1', 1)
for i in range(5):
    t=threading.Thread(target=b.worker, args=(str(i),))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

'''
test.SharePtr()
a=test('thread1', 1)
a.test_print()
p=[1, 1, 1]
print('before modified', p)
a.pass_addr(p)
print('after modified', p)
'''
