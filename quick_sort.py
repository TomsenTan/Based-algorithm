#-*-coding:utf8-*-
#快速排序
#算法要点：
#1.快速排序是基于递归和分治算法实现的一个算法，凡是利用递归实现的分治算法，时间
#复杂度都大概是nlog2n
#2.选定一个标准值，将数组/列表分成两半（分治算法思想），大于基准值的放右边的序列，
#小于基准值的放左边的序列。
#3. 递归实现1.2.过程实现快速排序

##快排与分治-归并算法的不同点在于，快排在拆分的过程已经将数组分为大小两部分，合并
##是通过递归实现的。
##而分治-归并算法是在合并的时候才将无序的数组变成有序，合并是通过比较左右两个数组
##中所有的元素来实现的。


#算法时间复杂度 O(nlog2n),空间复杂度O(nlog2n)
#空间复杂度计算：每次递归，同级递归中所有元素都需要放入序列中，空间为O(n),共需要
#递归log2n次

def quicksort(array):
    if len(array) < 2:     #递归出口
        return array
    else:
        pivot_index = 0     #元素的选择上可以进一步优化
        pivot = array[pivot_index]
        left_part = [i for i in array[pivot_index+1:] if i <= pivot]
        right_part = [i for i in array[pivot_index + 1:] if i > pivot]
        return quicksort(left_part) + pivot + quicksort(right_part)


def test_quicksort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    assert quicksort(seq) == sorted(seq)

