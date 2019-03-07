#-*-coding:utf8-*-
# 堆排序算法上的要点在于两个步骤的操作
# 1. 构造堆
# 2. 对换堆顶元素和堆最后一个元素


# 数据列表,由于python的list是线性数组，下标从0开始，而堆的下标需要从1开始
# 并且list没有从左端插入数据的方式，因此需要使用collections模块的deque双端队列
from collections import deque
mess_l = deque([30, 18, 20, 60, 90, 80, 48, 55])
mess_l.appendleft(0)
# print(mess_l)

def heap_adjust(L, start, end):
    '''
    构造堆，很关键的调整函数。下面以构造大顶堆为例
    从堆的最小子树开始，从下往上，从右往左，直到构建出大顶堆
    '''
    temp = L[start]
    i = start
    j = i * 2
    while j <= end:
        if (j < end) and (L[j] < L[j+1]):
            j += 1             # 使得L[j]是子树中最大值
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = i * 2
        else:               # 否则L[i]不变
            break
    L[i] = temp


def param_swap(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L

def heap_sort(L):
    L_Length = len(L) - 1
    first_sort_pos = int(L_Length/2)

    for i in range(first_sort_pos):
        heap_adjust(L, first_sort_pos-i, L_Length)  # start 每一次-1，从4-3-2-1

    for i in range(L_Length-1):             # 将顶值与最后一个值对换，再调整，保持顶值最大；则最后得出的是从小到达的序列
        L = param_swap(L, 1, L_Length-i)
        print(L)
        heap_adjust(L, 1, L_Length-i-1)

    return [L[i] for i in range(1, len(L))]

print(heap_sort(mess_l))




