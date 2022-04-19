from unionfind import UnionFind

class HexHuman:

    def update(self, steps):
        """
        更新棋盘步骤状态
        
        :param steps: HexGame中的steps
        :type steps: list
        :rtype: None
        """
        self.steps = steps
    
    def __init__(self, steps, column):
        """
        这是一个人类玩家的实例
        
        :param steps: 步数
        :type steps: list
        :param column: 棋盘阶数
        :type column: int
        """
        self.column = column
        self.steps = steps
        self.union_find = UnionFind(column*column, column)  # 玩家1的下棋位置的并查集
        pass
