#-*-coding:utf8-*-
#二分查找算法

def  binary_search(sorted_array,value):   #列表必须是有序的
    if not sorted_array:
        return -1

    beg = 0
    end = len(sorted_array)-1

    while beg<=end:
        mid = int((beg+end)/2)  #0.5也转化为整型
        if  sorted_array[mid] == value:
            return value
        elif sorted_array[mid]>value:
            end = mid - 1
        else:
            beg = mid + 1
    return -1


import bisect