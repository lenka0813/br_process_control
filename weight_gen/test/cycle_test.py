import numpy as np
import cyclequeue as cycle
import threading
# import network_engine as engine

import os
import sys

cur_dir = os.getcwd()
sys.path.append (cur_dir)

out = []
queue = cycle.cyclequeue(8)
tasks = [1,2,3,4,5,6,7,8,9]
queue.push(tasks)

queue.setQueueAvaliable()
queue.push(tasks)

ret = queue.assign(tasks)
queue.pop()
queue.pop()
queue.pop()
# queue.pop(out)
#print('out',out)
# queue.static_list()
# ret = queue.setQueueUnavaliable()
for i in range(20):
    out.clear()
    queue.static_list()
    if i != 4:  
        queue.pop(out)
    else:
        queue.setQueueUnavaliable()
    if i == 6:
        queue.setQueueAvaliable()
    if i%2 == 0:
        queue.push([2])
    print(i, out)    
print(ret)

# exec_engine = engine.exector(4)
