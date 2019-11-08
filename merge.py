import time

def cal_time(func):
    def out_t(*args,**kwargs):
        t1=time.time()
        res=func(*args,**kwargs)
        t2=time.time()
        print('%s的运行时间是%ss'%(func.__name__,t2-t1))
        return res
    return out_t

def merge(li,low,mid,hight):    #一次归并
    i=low
    j=mid+1
    tem_l=[]
    while i<=mid and j<=hight:
        if li[i]<li[j]:
            tem_l.append(li[i])
            i+=1
        else:
            tem_l.append(li[j])
            j+=1
    while i<=mid:
        tem_l.append(li[i])
        i+=1
    while j<=hight:
        tem_l.append(li[j])
        j+=1

    for i in range(low,hight+1):
        li[i]=tem_l[i-low]


def merge_sort(li,low,hight):
    if low<hight:
        mid=(low+hight)//2
        print('前半部分分解',li[low:mid+1])
        print('后半部分分解',li[mid+1:hight+1])
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,hight)
        merge(li,low,mid,hight)
        print('前半部分组合',li[low:mid+1])
        print('后半部分组合',li[mid+1:hight+1])

@cal_time
def main():
    li=[10,4,6,3,8,2,5,7,1,9]
    merge_sort(li,0,len(li)-1)
    print(li)


if __name__ == "__main__":
    main()



