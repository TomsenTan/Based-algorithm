#-*-coding:utf8-*-
#选择排序
#算法要点：
#1.每次循环假定循环比较的数据的第一个数为最小值，
#将后面的数与其比较找到最小值，并将最小值与第一个数比较
#2.下一次循环就可以在range(len-i-1)即前一次冒泡比较次数基础上减一
# （即减去已经排好的前面数据的个数）
#总结来说每次都选择一个最小的数放在最前面

#平均时间复杂度为O(n2);空间复杂度为O(n),实际为O(n+1)

#算法实现：
import random

def select_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1,n):    #遍历后面的所有元素
            if seq[j]<seq[min_idx]:
                min_idx = j
                print(seq)
        if min_idx!=i:
            seq[i],seq[min_idx] = seq[min_idx],seq[i]
    return seq

#单元测试
def test_select_sort():
   seq = list(range(10))
   random.shuffle(seq)
   select_sort(seq)
   assert seq == sorted(seq)

test_select_sort()