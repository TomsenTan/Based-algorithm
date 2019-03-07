#-*-coding:utf8-*-
#Date:2018-12-18
#Author：Thomson

#邻接集表示有向图
# a,b,c,d,e,f = range(6)   #分别表示0-5

# N=[
#     {b},   #a
#     {c},   #b
#     {a,d},   #c
#     {e},   #d
#     {f},   #e
#     {d}    #f
# ]

#邻接字典表示有向图
N={
    "a":{"b"},   #a
    "b":{"c"},   #b
    "c":{"a","d","g"},   #c
    "d":{"e"},   #d
    "e":{"f"},   #e
    "f":{"d"},    #f
    "g":{"h"},
    "h":{"i"},
    "i":{"g"}
}

from collections import OrderedDict

'''
无向图的算法实现
'''

#找出图的连通分量(无向图）
def componets(G,start):
    comp = []
    seen = set()    #遍历过的节点
    for u in G:
        for v in G[u]:
            if v in seen:
                continue
            C = walk(G,v)
            seen.update(C)
            comp.append(C)
    return comp

#单元测试
# print(componets(N,"a"))



#递归实现深度优先搜索（拓扑排序）
def  dfs_sort(G):
    S,result = set(),[]
    def recurse(u):          #递归算法
        for i in u:
            if i in S:
                return
        S.union(u)
        for v in u:       #递归搜索下一节点
            recurse(G[v])
        result.append(u)     #直到递归底部
    for u in G:
        recurse(u)

    result.reverse()         #将递归的结果翻转，得到正序遍历结果
    return result


'''
有向图的算法实现
'''

#递归实现深度优先排序
def rec_dfs(G,s,S=None):
    if S is None:
        #S = set()    #集合存储已经遍历过的节点
        S = list()    #用列表可以更方便查看遍历的次序，而用集合可以方便用difference求差集
    # S.add(s)
    S.append(s)
    # print(S)
    for u in G[s]:
        if u in S:continue
        rec_dfs(G,u,S)
    return S

#单元测试
# print(rec_dfs(N,0))


#翻转图
def re_tr(G):
    GT = {}
    for u in G:
        for v in G[u]:
            # print(GT)
            if GT.get(v):
                GT[v].add(u)
            else:
                GT[v] = set()
                GT[v].add(u)

    return GT

#遍历有向图的强连通分量
def walk(G,start,S=set()):
    P,Q = dict(),set()   #list存放遍历顺序，set存放已经遍历过的节点
    P[start] = None
    Q.add(start)
    while Q:
        u = Q.pop()                      #选择下一个遍历节点（随机性）
        for v in G[u].difference(P,S):   #返回差集
            Q.add(v)
            P[v] = u
    print(P)
    return P


#获得各个强连通图
def scc(G):
    GT = re_tr(G)
    sccs,seen = [],set()
    for u in rec_dfs(G,"a"):    #以a为起点
        if u in seen:continue
        C = walk(GT,u,seen)
        seen.update(C)
        sccs.append(C)
    return sccs

print(scc(N))

#单元测试
# print(re_tr(N))


#强连通分量的遍历
# print(re_tr(N))
# print(rec_dfs(re_tr(N),"e"))

