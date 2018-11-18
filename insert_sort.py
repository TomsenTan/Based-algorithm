#-*-coding:utf8-*-
#插入排序
#算法要点：
#1.每次循环有序序列后面的一位数与前面的有序序列进行比较，插入到比这位数小的数后面
#每次循环都将大于这个数的数往后移动。
#2.每次循环比较的次数是无法确定的，但所有比较次数的总和会趋于一个值

#时间：o(n2)  空间：0(n+1)
#代码实现
import random

def insert_sort(seq):
    n = len(seq)
    for i in range(1,n):
        value = seq[i]   #保存这个数，因为移动过程中数据往后移动会覆盖这个数
        pos = i
        while pos>0 and value<seq[pos-1]:
            seq[i] = seq[i-1]
            pos -= 1
        seq[pos] = value
        print(seq)

#单元测试：
def test_insert_sort():
   seq = list(range(10))
   random.shuffle(seq)
   insert_sort(seq)
   assert seq == sorted(seq)

test_insert_sort()
