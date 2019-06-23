// network distribution calculate engine

#define MAX_WORKER_NUM 8


class exector {
	exector();
	~exector();
    
    bool add_task()
    {
        task_count++;
        if(task_count > = MAX_WORKER_NUM) return;
    }
    
    // function
    void static_list()
    
    void clear()
    {
        if( task_count ==0) 
        {
            printf("[WARN] no task is in the taskqueue.\n");
            return;    
        }
        for(int i=0; i < task_count; i++)
        {
            finished[i] = 0;
            running[i] = 0;
        }
        taskqueue.clear();
        printf("[INFO] task in the taskqueue is clean.\n");
    }
	
	// 建立线程池（worker池）
	void build()
	{
		
	}
    void save(char *path)
    {
    }
    
    void load(char *path);
/* 	
    1.	下发任务，设定模型参数，启动线程组
	2.	等待每个线程执行完毕
	3.	每个线程执行完毕，检查该次任务下发的状态是否都收集，并检查是否有停止信号。
		若继续等待，但是进行睡眠前，检查各worker状态，防止漏掉。
	4.	由第一个注册node进行参数合并（合并策略？），并设计终止条件
*/
	void proxy()
	{ 
        int print_count=0;
        char task_num =0;
        bool proxy_status = true;
        while(1) {
            task_num = task_count;
            network_model= task_queue[0];
            clear();
            // check the engine status
            if(!is_stop || !proxy_status)
            {
                is_stop = false;
                for(int i=0; i < task_num; i++)
                {
                    taskqueue.push(network_model());
                } 
                printf("[INFO] The proxy is exit success.\n");
                break;
            }
            print_count ++;
            printf("=========new %d iter is start========\n", print_count);
            for(int i=0; i < task_num; i++)
            {
                taskqueue.push(network_model);
            }   
            while(1) 
            { 
                char running_num = 0;
                char task_already = 0;
                
                // wait taskfinish;
                for(int i=0; i < task_num; i++)
                {
                    if( finished[i] == 1)
                    {
                        task_already++;
                    }
                    if( running[i] ==1) 
                    {
                        running_num++;
                    }
                }
                char check_num = running_num + task_already;
                if(check_num != task_num) 
                {
                    printf("[ERROR] running time is out of control\n");
                    proxy_status = false;
                    clear();
                    break;
                }
                
                if(task_already != task_num) 
                {
                    if(print_count%(task_num%2) == 0) 
                    {
                        printf("[INFO]: There are %d task is running\n", task_num-task_already);
                    }
                    continue;
                }
                
                bool ret = network_model.concat(task_queue);
                //set the task status
                clear();
                // check the model maturity
                if(ret == false) 
                {
                    is_stop=false;
                    break;
                }
            } //end of dispatch 
        } // end of proxy 
        clear();        
	}
/*
	1.	是否有新的任务下发，否则继续等待
	2.	设置状态位（0 running、1 finished）
	3.	是否是停止信号
	4.	用户提交的类模型计算，更新
	5.	更新worker状态
	6.	跳转到1
*/
    void worker (network_model, id) 
	{
        char id_=id;
        if(id_ > = MAX_WORKER_NUM)
        {
            return;
        }
		while(1)
		{   
	        //wait taskqueue
            
            // check status
			if(!is_stop|| !enable[id_]) {
				printf(" 第几号worker退出\n");
				break;
            }
            
            if( finished[id_] == 1 || running[id_] == 1) 
            {
                //singal, the task is busy
                continue;
            }
            running[id_]=1;
            finished[id_]=0;
            
            network_model.cal();
            
            finished[id_]=1;
            running[id_]=0;
            
            //signal taskqueue
        }
	}
    
	void exec()
	{
        bool ret = false;
        // build proxy and work thread
		ret = build();
        if(ret == false) 
        {
            printf("[ERROR] start init fail.\n");
            return;
        }
        // do some interface 
        int n=0;
        
        while(1)
        {
            n << cin;
            if( n < 0 || n > 10) 
            {
                printf("[ERROR] unsupport cmd code.\n");
                printf(" 0: exit 1: static_list 2: add_task 3: restart \n");  
            }
            switch(n) 
            {
                case 0: // exit the system
                        save();
                        is_stop = false ;
                        break;
                case 1: // show the status
                        static_list();
                        break;
                case 2: // add the task num
                        add_task();
                        break;
                case 3: // restart 
                        dispatch()
                        break();     
            }
            n=0;
        }
        
	}
	void dispatch 
    {
        proxy()
    }
	
	void sync()
	{
		
	}
    vector<network_model>task_queue;
    singal taskqueue;
    singal taskfinish;
	char running[MAX_WORKER_NUM];
	char finished[MAX_WORKER_NUM];
    char enable[MAX_WORKER_NUM];
	bool is_stop;
    char task_count;
};