import time
import random

def col_time(func):
    def out_f(*args,**kwargs):
        t1=time.time()
        res =func(*args,**kwargs)
        t2=time.time()
        print('%s 的时间是%s s' %(func.__name__,t2-t1))
        return res
    return out_f


def insert_sort(li):
    for i in range(1,len(li)):
        temp=li[i]
        while i-1>=0 and li[i-1]>temp:
            li[i]=li[i-1]
            i-=1
        li[i]=temp


def main():
    lists=[3,5,6,7,8,2,9,4,1]
    insert_sort(lists)
    print(lists)

@col_time
def list_time():
    lists=list(range(1000,0,-1))
    random.shuffle(lists)
    insert_sort(lists)
    # print(lists)

if __name__ == "__main__":
    # main()
    list_time()
    
