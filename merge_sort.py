#-*-coding:utf8-*-
#分治算法
#分治是一种思想，分治和归并算法有很多种变形，这里谈两种情况
#1.两个无序的数组合并  2.一个无序的数组用分治合并算法实现排序

#以上两种情况时间复杂度都为O(log2n),空间复杂度都为O(n)

#一个无序数组分治-归并算法实现
def  merge_sort(seq):
    if len(seq)<=1:
        return seq   #递归出口，有可能序列只有一个元素，也可能使递归二分到只有一个元素
    else:
        mid = len(seq)//2
        left_half = merge_sort(seq[:mid])  #递归将左右两边拆分,如果没到出口是不会调用merge_list
        right_half = merge_sort(seq[mid:])
        new_seq = merge_list(left_half,right_half)

        return new_seq

def merge_list(left,right):   #合并两个有序数组,以左右数组表示
    length_left = len(left)
    length_right = len(right)
    a=b=0
    new_list = []
    while a< length_left and b <length_right:   #排序两个数组
        if left[a] < right[b]:
            new_list.append(left[a])
            a+=1
        else:
            new_list.append(right[b])
            b+=1

    while a< length_left:
        new_list.append(left[a])
        a+=1

    while b< length_right:
        new_list.append(right[b])
        b+=1

    return new_list

#两个无序数组的合并
#需要先将两个数组用快排排序后再合并