import time

# 统计时间装饰器
def col_time(func):
    def out_time(*args,**kwargs):
        t1=time.time()
        res=func(*args,**kwargs)
        t2=time.time()
        print('%s 的时间是 %s s'%(func.__name__,t2-t1))
        return res
    return func
