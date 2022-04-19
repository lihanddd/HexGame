from unionfind import UnionFind
from random import randint
import time


class HexAI:

    def count_empty(self):
        cnt = 0
        for i in range(self.column):
            for j in range(self.column):
                pos = (i, j)
                cnt_ = 0
                if not (pos[0]+1, pos[1]) in self.steps:
                    cnt_ = cnt_ + 1
                if not (pos[0]-1, pos[1]) in self.steps:
                    cnt_ = cnt_ + 1
                if not (pos[0], pos[1]+1) in self.steps:
                    cnt_ = cnt_ + 1
                if not (pos[0], pos[1]-1) in self.steps:
                    cnt_ = cnt_ + 1
                if not (pos[0], pos[1]+1) in self.steps:
                    cnt_ = cnt_ + 1
                if not (pos[0]+1, pos[1]-1) in self.steps:
                    cnt_ = cnt_ + 1
                if not (pos[0]-1, pos[1]+1) in self.steps:
                    cnt_ = cnt_ + 1
                if cnt_ >= 4:
                    cnt = cnt + 1
        return cnt

    def vertical_score(self):
        """
        棋盘中某个自己的棋，离边线越近，则越有可能连起来
        因为我们期望能尽快和边线连起来，对我们更有利
        表征一个垂直的纵向特征
        返回一个MAX-min(离一个边的距离，离另一个边的距离)

        :return: 分数
        :rtype: int
        """
        # TODO
        score = 0
        return score

    def side_point_score(self):
        """
        棋盘里属于我们的边线上，若有我们更多的棋子，
        则意味着更多的连接路线，对我们更有利。
        num++
        棋盘里属于敌人的边线上，若有我们更多的棋子，
        则意味着敌人更少的连接路线，对我们更有利。
        num--
        返回一个较中的分数*num

        :return: 分数
        :rtype: int
        """
        # TODO
        score = 0
        return score

    def killer_pos_score(self):
        """
        棋盘上如果有一个或多个位置，放置我们的棋子后游戏胜利，
        则num++
        棋盘上如果有一个或多个位置，对手放置棋子后对手游戏胜利，
        则num--
        返回一个次高的分数*num

        :return: 分数
        :rtype: int
        """
        # TODO
        score = 0
        return score

    def stronger_pos_score(self):
        """
        棋盘上如果有一个或多个位置，放置我们的棋子后连通两个分量，
        则num++
        棋盘上如果有一个或多个位置，对手放置棋子后对手连通两个分量，
        则num--
        返回一个较高的分数*num

        :return: 分数
        :rtype: int
        """
        # TODO
        score = 0
        return score

    def spread_score(self):
        """
        棋盘上我们的分布越散，越意味着有更多的可能
        num = 分支个数（包括单独一个棋子）
        basic_score = 100
        我们希望一上来棋盘走的分散些，之后慢慢收敛，
        所以一开始返回一个很大的basic_score*num，
        之后每一次下棋basic_score*0.8，返回basic_score*num

        :return: 分数
        :rtype: int
        """
        self.turn = self.turn+1
        score = 0
        basic_score = 100
        sub_set = []
        i = len(self.steps) - 1
        cnt = 0
        while i >= 0:
            if self.union_find.find(self.steps[i]) not in sub_set:
                sub_set.append(self.steps[i])
                cnt += 1
            i -= 2
        score = basic_score * pow(0.8, self.turn) * cnt

        return score

    def empty_score(self):
        """
        我们希望棋盘上可扩展分支更多，这样意味着更多的可能，
        每一个棋子周围有六个相邻位置
        num = 棋盘上以我们棋子为中心，同时相邻的无人下棋的位置>=4的个数
        basic_score = 100
        一开始返回一个很大的basic_score*num，
        之后每一次下棋basic_score*0.8，返回basic_score*num

        :return: 分数
        :rtype: int
        """
        begin = time.time()
        score = 0
        basic_score = 100
        cnt = self.count_empty()
        score = score + basic_score * pow(0.8, self.turn) * cnt
        end = time.time()
        self.empty_score_time = self.empty_score_time + end - begin
        return score

    def random_score(self):
        """
        为棋盘增加随机性

        :return: 分数
        :rtype: int
        """
        score = randint(0, 100)
        return score

    def evaluate_board(self):
        """
        评估当前board的分数
        (加和pos位置所有项目分数)

        :return: total score
        :rtype: int
        """
        # 调用上面所有子项目评分后加和，记得补充新加的项目
        scores = 0
        # scores = scores + self.random_score()+self.vertical_score()+self.killer_pos_score() + \
        #     self.side_point_score()+self.stronger_pos_score() + \
        #     self.spread_score()+self.empty_score()
        scores = scores + self.random_score()+self.vertical_score()+self.killer_pos_score() + \
            self.side_point_score()+self.stronger_pos_score() + \
            self.spread_score()

        return scores

    def update(self, steps):
        """
        更新棋盘步骤状态

        :param steps: HexGame中的steps
        :type steps: list
        :rtype: None
        """
        self.steps = steps

    def choose(self):
        """
        极大极小搜索选择下棋位置

        :return: 决策后的坐标
        :rtype: (int, int)
        """
        global cut_count   # 统计剪枝次数
        cut_count = 0
        global search_count   # 统计搜索次数
        search_count = 0
        global next_i
        next_i = 0
        global next_j
        next_j = 0
        self.empty_score_time = 0
        self.negamax(self.depth, -99999999, 99999999)
        print("本次共剪枝次数：" + str(cut_count))
        print("本次共搜索次数：" + str(search_count))
        # print("count empty_score use ",self.empty_score_time)
        return (next_i, next_j)

    def negamax(self, depth, alpha, beta):
        """
        负值极大算法搜索 + alpha/beta剪枝

        :param depth: 树的搜索深度，必须为奇数
        :param alpha: 剪枝时传递的上限
        :param beta: 剪枝时传递的下限
        """
        if depth == 0:
            return self.evaluate_board()

        board = []
        for i in range(self.column):
            for j in range(self.column):
                board.append((i, j))
        blank_list = list(set(board).difference(set(self.steps)))
        # 遍历每一个候选步
        for next_step in blank_list:

            global search_count
            search_count += 1

            # # 如果要评估的位置没有相邻的子， 则不去评估  减少计算
            # if not has_neightnor(next_step):
            #     continue

            self.steps.append(next_step)
            value = -self.negamax(depth - 1, -beta, -alpha)
            self.steps.remove(next_step)

            if value > alpha:
                # print(str(value) + "alpha:" + str(alpha) + "beta:" + str(beta))
                if depth == self.depth:
                    global next_i
                    global next_j
                    next_i = next_step[0]
                    next_j = next_step[1]
                # alpha + beta剪枝点
                if value >= beta:
                    global cut_count
                    cut_count += 1
                    return beta
                alpha = value

        return alpha

    def __init__(self, steps, column, is_first_player, depth=3):
        """
        搜索主功能

        :param steps: 步数
        :type steps: list
        :param column: 棋盘阶数
        :type column: int
        """
        # TODO 极大极小搜索
        self.steps = steps
        self.column = column
        self.is_first_player = is_first_player
        self.depth = depth
        self.union_find = UnionFind(column*column, column)  # 玩家1的下棋位置的并查集
        self.turn = 0
        self.empty_score_time = 0
