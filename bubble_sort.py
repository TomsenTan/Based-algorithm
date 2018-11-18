#-*-coding:utf8-*-
#冒泡排序
#算法要点：
#每次循环将相邻两个数进行比较，可以将最大的数冒泡到最后
#下一次循环就可以在range(len-i-1)即前一次冒泡比较次数基础上减一

#时间：o(n2)  空间：0(n)
#代码实现
import random

def bubble_sort(seq):
    n = len(seq)
    for i in range(n-1):
        print(seq)
        for j in range(n-i-1):
            if seq[j]>seq[j+1]:
                seq[j],seq[j+1] = seq[j+1],seq[j]
    print(seq)

#单元测试
def test_bubble_sort():
   seq = list(range(10))
   random.shuffle(seq)
   bubble_sort(seq)
   assert seq == sorted(seq)

test_bubble_sort()