import sys
import random,time
sys.setrecursionlimit(1000000)

def cal_time(func):
    def out_t(*args,**kwargs):
        t1=time.time()
        res=func(*args,**kwargs)
        t2=time.time()
        print('%s运行时间是%s s' %(func.__name__,t2-t1))
        return res
    return out_t

def quick_sort(li,left,right):
    if left<right:   #至少有2个元素
        mid=partition(li,left,right)
        quick_sort(li,left,mid-1) 
        quick_sort(li,mid+1,right)

def partition(li,left,right):
    temp=li[left]
    while left < right:
        while left<right and li[right]>=temp:
            right-=1    
        li[left]=li[right]

        while left<right and li[left]<=temp:
            left+=1
        li[right]=li[left] 
    li[left]=temp
    return left


@cal_time
def count_t():
    lists=[3,5,6,7,8,2,9,4,1]
    quick_sort(lists,0,len(lists)-1)
    print(lists)

@cal_time
def test_t():
    lists=list(range(100000,0,-1))
    random.shuffle(lists)
    quick_sort(lists,0,len(lists)-1)

if __name__ == "__main__":
    # lists=[3,5,6,7,8,2,9,4,1]
    # quick_sort(lists,0,len(lists)-1)
    # print(lists)
    # print(partition(lists,0,len(lists)-1))
    # print(lists)
    count_t()
    # test_t()


