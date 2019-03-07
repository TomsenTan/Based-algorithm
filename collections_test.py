#-*-coding:utf8-*-
'''
此demo用于测试collecitons库里面的数据结构
Date:2018-11-21
'''

from  collections import deque,defaultdict,OrderedDict

d = deque()
#增加数据
d.append('1')
d.append('2')
d.appendleft('3')
l = ['4','5']
d.extend(l)
d.extendleft(l)
print(d)
d.insert(0,5)
print(d)
# d[1] = 3
# print(d[1])


#计算deque元素个数
print(d.count('5'))

#循环移动
d.rotate(1)
print(d)
d.rotate(-1)
print(d)


#计算股票和仓库存货常用的移动平均数
import itertools
def moving_average(iterable,n=3):
    it = iter(iterable)
    d = deque(itertools.islice(it,n-1))  #迭代出前2个数据
    print(d)
    d.appendleft(0)  #防止第一次运行算法时候把第一个数据删除
    s = sum(d)
    print(d)
    print(s)
    for elem in it:
        s += elem-d.popleft()
        d.append(elem)
        yield s/float(n)

l = [10,20,18,27,15]
for average in moving_average(l):
  print(average)


d = dict()
d["1"] = "one"
d["2"] = "two"
print(d["2"])


dd = defaultdict(lambda:"none")
dd["a"] = "apple"
dd["b"] = "banana"

print(dd["c"])
print(dd)


od = OrderedDict()
od["1"] = "one"
od["2"] = "two"
od["3"] = "three"
od["4"] = "four"
od["5"] = "five"
print(od)