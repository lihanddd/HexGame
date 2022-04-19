class UnionFind:
    """并查集类"""
    
    def __init__(self, n, column):
        """
        长度为n的并查集
        指并查集中独立的集合个数
        
        :param n:
        :return:
        """
        self.column = column
        self.f = []  # 每个独立集合的代表元素
        self.uf = [-1 for i in range(n)]  # 每个节点的父亲节点
        self.count = n
    
    def get_id(self, i, j):
        return self.column * i + j

    def get_pos(self, n):
        return (int(n) // self.column, n % self.column)
    
    def find(self, p):
        """
        查找p的根结点(祖先)
        
        :param p: 要查找的节点
        :return: 节点祖先
        """
        if isinstance(p, tuple):
            p = self.get_id(p[0], p[1])
        
        r = p
        while self.uf[p] >= 0:
            p = self.uf[p]
        while r != p:
            self.uf[r], r = p, self.uf[r]
        return p
    
    def union(self, p, q):
        """
        连通p,q 让q指向p
        
        :param p:
        :param q:
        :return: None
        """
        if isinstance(p, tuple):
            p = self.get_id(p[0], p[1])
        if isinstance(q, tuple):
            q = self.get_id(q[0], q[1])
        
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        elif self.uf[p_root] > self.uf[q_root]:  # 负数比较, 左边规模更小
            self.uf[q_root] += self.uf[p_root]
            self.uf[p_root] = q_root
        else:
            self.uf[p_root] += self.uf[q_root]  # 规模相加
            self.uf[q_root] = p_root
        self.count -= 1  # 连通后集合总数减一
    
    def is_connected(self, p, q):
        """
        判断pq是否已经连通
        
        :param p:
        :param q:
        :return:
        """
        return self.find(p) == self.find(q)
    
    def get_size(self, p):
        """
        获得含有元素p的子集的元素个数
        
        :param p: 所下位置
        :return: 元素个数
        """
        return -self.uf[self.find(p)]
    
    def add(self, p):
        """
        海克斯棋下棋位置为p，更新并查集

        :param p: 所下位置
        :return: NONE
        """
        x = p[0]
        y = p[1]
        flag = 0
        column = self.column
        if x - 1 >= 0 and self.get_pos(self.find((x - 1, y))) in self.f:
            self.union((x - 1, y), (x, y))
            flag = 1
        if y - 1 >= 0 and self.get_pos(self.find((x, y - 1))) in self.f:
            self.union((x, y - 1), (x, y))
            flag = 1
        if x + 1 < column and self.get_pos(self.find((x + 1, y))) in self.f:
            self.union((x + 1, y), (x, y))
            flag = 1
        if y + 1 < column and self.get_pos(self.find((x, y + 1))) in self.f:
            self.union((x, y + 1), (x, y))
            flag = 1
        if y + 1 < column and x - 1 >= 0 and self.get_pos(self.find((x - 1, y + 1))) in self.f:
            self.union((x - 1, y + 1), (x, y))
            flag = 1
        if x + 1 < column and y - 1 >= 0 and self.get_pos(self.find((x + 1, y - 1))) in self.f:
            self.union((x + 1, y - 1), (x, y))
            flag = 1
        if flag == 0:
            self.f.append((x, y))
