#-*-coding:utf8-*-
#二叉树的构造
#原理：首先要构造好根节点，父节点以及父节点和子节点的指向关系，因为python没有链表结构，
#所以在构建指向关系的时候需要定义一种关联关系，实现上用字典表示


#例如构造如下一个二叉树
#              A
#            /   \
#           B     C
#          / \   /  \
#         D   E  F   G
#            /      / \
#           H      I   J
#
#


#初始化数据
node_list = [
    {'data':'A','left':'B','right':'C','is_root':True},
    {'data':'B','left':'D','right':'E','is_root':False},
    {'data':'C','left':'F','right':'G','is_root':False},
    {'data':'D','left':None,'right':None,'is_root':False},
    {'data':'E','left':'H','right':None,'is_root':False},
    {'data':'F','left':None,'right':None,'is_root':False},
    {'data':'G','left':'I','right':'J','is_root':False},
    {'data':'H','left':None,'right':None,'is_root':False},
    {'data':'I','left':None,'right':None,'is_root':False},
    {'data':'J','left':None,'right':None,'is_root':False},
]

#构造节点
class BinTreeNode(object):
    def __init__(self,data,left=None,right=None):
        self.data,self.left,self.right = data,left,right


#构造树
class BinTree(object):
    def __init__(self,root=None):
        self.root = root

    @classmethod
    def built_from(cls,node_list):
        '''
        :param node_list
        :return:root
        第一次遍历构造所有的node节点
        第二次遍历给多有节点（包括root和孩子节点)赋值
        '''

        node_dict = {}
        #构造node节点
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)  #字典中存放的是类实例（node节点）
        #给root和孩子赋值
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]     #获取字典中的节点（类实例）
            if node_data['is_root']:
                root = node            #给树的根节点赋值
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return BinTree(root)

    def preorder_trav(self,subtree):
        '''
        先根遍历
        :param subtree:
        '''
        if subtree is not None:
            print(subtree.data)
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)

btree = BinTree.built_from(node_list)
btree.preorder_trav(btree.root)
