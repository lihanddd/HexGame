from hexgameboard import HexGameBoard
from unionfind import UnionFind
from hexai import HexAI
from hexhuman import HexHuman

class HexGame:
    
    def move(self, player, pos):
        """
        下棋
        
        :param player: 玩家 0 或 1
        :param pos: 所下位置
        :return: 下棋是否成功
        """
        if not self.board.over_bound(pos) and pos not in self.steps:  # 检查位置合法性
            self.steps.append(pos)
            self.board.colorize(player, pos)
            return True
        return False
    
    def judge(self, player):
        """
        判断胜负
        
        :param player: 玩家
        :return: True表示玩家获胜
        """
        ai_union_find = self.ai.union_find if player==1 else None
        human_union_find = self.human.union_find if player==0 else None
        column = self.board.column
        new_piece = self.steps[self.steps.__len__() - 1]  # 将新棋子加入到并查集中
        if player == 0:
            human_union_find.add(new_piece)
        else:
            ai_union_find.add(new_piece)

        if player == 0:
            for i in range(column):
                for j in range(column):
                    if human_union_find.is_connected((0, i), (column - 1, j)):  # 红色胜
                        return 1
        
        else:
            for i in range(column):
                for j in range(column):
                    if ai_union_find.is_connected((i, 0), (j, column - 1)):  # 蓝色胜
                        return 1
    
    def ai_choose(self):
        """
        AI决策
        
        :param player: AI所属玩家
        :return: AI决策位置
        """
        self.ai.update(self.steps)
        next_pos = self.ai.choose()
        return next_pos
    
    def start_game(self):
        """
        开始游戏，玩家0为人类，玩家1为AI
        
        :param first_player: 先手玩家，默认为玩家0
        :return: 返回获胜的玩家
        """
        first_player = self.first_player
        while True:
            if first_player == 0:
                while not self.move(0, self.board.getpos()):
                    continue
                if self.judge(0):
                    return 0
            while True:
                if self.move(1, self.ai_choose()):
                    break
            if self.judge(1):
                return 1
            if first_player == 1:
                while not self.move(0, self.board.getpos()):
                    continue
                if self.judge(0):
                    return 0
    
    def show_winner(self, winner):
        """
        在棋盘上展示胜利者信息
        
        :param winner: 胜者
        :rtype: None
        """
        self.board.show_message("玩家%d获胜，点击任意处退出" % winner)
    
    def __init__(self, column=11, first_player=0):
        """
        Initial a hex game
        棋盘位置标记方式 n = 10 * i + j
        
        :param column: 棋盘阶数，默认为11
        """
        self.first_player = first_player
        self.board = HexGameBoard(column)
        self.steps = []  # 步骤记录，通过奇偶表示玩家
        self.ai = HexAI(self.steps, column, first_player==1, depth=3)
        self.human = HexHuman(self.steps, column)
    
    def __del__(self):
        self.board.getpos()
        del self.board
