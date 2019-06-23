
import network_engine as engine
import time

def task(id ):
    print('worker run'%(id))
    
exector = engine.exector(4)

# define train task, with the template.py format
exector.add_task(task, 6)
exector.assign_task(1)

ret = exector.build()
if ret is not False:
    for i in range(3):
        exector.proxy()
        print('[INFO] after proxy')
        time.sleep(2)

print('start ok')