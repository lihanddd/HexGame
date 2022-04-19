import graphics
from math import sqrt

class HexGameBoard:
    COLOR = ['red', 'blue']  # 玩家代表色
    
    def draw_hexagon(self, left_point_x, left_point_y):
        """
        绘制一个六边形
        
        :param left_point_x: 六边形最左边点X坐标
        :param left_point_y: 六边形最左边点Y坐标
        :return: self
        """
        graphics.Polygon(graphics.Point(left_point_x, left_point_y),
                         graphics.Point(left_point_x + self.HEXAGON_SIDE_LENGTH / 2,
                                        left_point_y + self.HEXAGON_HALF_HEIGHT),
                         graphics.Point(left_point_x + 3 * self.HEXAGON_SIDE_LENGTH / 2,
                                        left_point_y + self.HEXAGON_HALF_HEIGHT),
                         graphics.Point(left_point_x + 2 * self.HEXAGON_SIDE_LENGTH, left_point_y),
                         graphics.Point(left_point_x + 3 * self.HEXAGON_SIDE_LENGTH / 2,
                                        left_point_y - self.HEXAGON_HALF_HEIGHT),
                         graphics.Point(left_point_x + self.HEXAGON_SIDE_LENGTH / 2,
                                        left_point_y - self.HEXAGON_HALF_HEIGHT)).draw(self.win)
        return self
    
    def draw_line_blue(self, pos):
        """
        绘制棋盘中蓝线
        
        :param pos:
        :return: None
        """
        pt1 = (0, self.height / 2)
        pt2 = (self.HEXAGON_SIDE_LENGTH / 2, self.height / 2 + self.HEXAGON_HALF_HEIGHT)
        pt3 = (self.HEXAGON_SIDE_LENGTH * 3 / 2, self.height / 2 + self.HEXAGON_HALF_HEIGHT)
        l1 = graphics.Line(
            graphics.Point(pt1[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt1[1] + self.HEXAGON_HALF_HEIGHT * pos),
            graphics.Point(pt2[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt2[1] + self.HEXAGON_HALF_HEIGHT * pos))
        l1.setWidth(10)
        l1.setFill('blue')
        l1.draw(self.win)
        l2 = graphics.Line(
            graphics.Point(pt2[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt2[1] + self.HEXAGON_HALF_HEIGHT * pos),
            graphics.Point(pt3[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt3[1] + self.HEXAGON_HALF_HEIGHT * pos))
        l2.setWidth(10)
        l2.setFill('blue')
        l2.draw(self.win)
        
        pt4 = (self.HEXAGON_SIDE_LENGTH / 2 + (self.column - 1) * self.HEXAGON_SIDE_LENGTH * 3 / 2,
               self.height / 2 - self.HEXAGON_HALF_HEIGHT - (self.column - 1) * self.HEXAGON_HALF_HEIGHT)
        pt5 = (self.HEXAGON_SIDE_LENGTH * 3 / 2 + (self.column - 1) * self.HEXAGON_SIDE_LENGTH * 3 / 2,
               self.height / 2 - self.HEXAGON_HALF_HEIGHT - (self.column - 1) * self.HEXAGON_HALF_HEIGHT)
        pt6 = (self.HEXAGON_SIDE_LENGTH * 2 + (self.column - 1) * self.HEXAGON_SIDE_LENGTH * 3 / 2,
               self.height / 2 - (self.column - 1) * self.HEXAGON_HALF_HEIGHT)
        l3 = graphics.Line(
            graphics.Point(pt4[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt4[1] + self.HEXAGON_HALF_HEIGHT * pos),
            graphics.Point(pt5[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt5[1] + self.HEXAGON_HALF_HEIGHT * pos))
        l3.setWidth(10)
        l3.setFill('blue')
        l3.draw(self.win)
        l4 = graphics.Line(
            graphics.Point(pt5[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt5[1] + self.HEXAGON_HALF_HEIGHT * pos),
            graphics.Point(pt6[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt6[1] + self.HEXAGON_HALF_HEIGHT * pos))
        l4.setWidth(10)
        l4.setFill('blue')
        l4.draw(self.win)
    
    def draw_line_red(self, pos):
        """
        绘制棋盘中红线
        
        :param pos:
        :return: None
        """
        pt1 = (0, self.height / 2)
        pt2 = (self.HEXAGON_SIDE_LENGTH / 2, self.height / 2 - self.HEXAGON_HALF_HEIGHT)
        pt3 = (self.HEXAGON_SIDE_LENGTH * 3 / 2, self.height / 2 - self.HEXAGON_HALF_HEIGHT)
        l1 = graphics.Line(
            graphics.Point(pt1[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt1[1] - self.HEXAGON_HALF_HEIGHT * pos),
            graphics.Point(pt2[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt2[1] - self.HEXAGON_HALF_HEIGHT * pos))
        l1.setWidth(10)
        l1.setFill('red')
        l1.draw(self.win)
        l2 = graphics.Line(
            graphics.Point(pt2[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt2[1] - self.HEXAGON_HALF_HEIGHT * pos),
            graphics.Point(pt3[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt3[1] - self.HEXAGON_HALF_HEIGHT * pos))
        l2.setWidth(10)
        l2.setFill('red')
        l2.draw(self.win)
        
        pt4 = (self.HEXAGON_SIDE_LENGTH / 2 + (self.column - 1) * self.HEXAGON_SIDE_LENGTH * 3 / 2,
               self.height / 2 + self.HEXAGON_HALF_HEIGHT + (self.column - 1) * self.HEXAGON_HALF_HEIGHT)
        pt5 = (self.HEXAGON_SIDE_LENGTH * 3 / 2 + (self.column - 1) * self.HEXAGON_SIDE_LENGTH * 3 / 2,
               self.height / 2 + self.HEXAGON_HALF_HEIGHT + (self.column - 1) * self.HEXAGON_HALF_HEIGHT)
        pt6 = (self.HEXAGON_SIDE_LENGTH * 2 + (self.column - 1) * self.HEXAGON_SIDE_LENGTH * 3 / 2,
               self.height / 2 + (self.column - 1) * self.HEXAGON_HALF_HEIGHT)
        l3 = graphics.Line(
            graphics.Point(pt4[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt4[1] - self.HEXAGON_HALF_HEIGHT * pos),
            graphics.Point(pt5[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt5[1] - self.HEXAGON_HALF_HEIGHT * pos))
        l3.setWidth(10)
        l3.setFill('red')
        l3.draw(self.win)
        l4 = graphics.Line(
            graphics.Point(pt5[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt5[1] - self.HEXAGON_HALF_HEIGHT * pos),
            graphics.Point(pt6[0] + (3 / 2) * self.HEXAGON_SIDE_LENGTH * pos, pt6[1] - self.HEXAGON_HALF_HEIGHT * pos))
        l4.setWidth(10)
        l4.setFill('red')
        l4.draw(self.win)
    
    def getpos(self):
        """
        获取鼠标点击位置的格子坐标
        
        :return: None
        """
        point = self.win.getMouse()
        pt = (self.HEXAGON_SIDE_LENGTH, self.height / 2)
        x = point.getX()
        y = point.getY()
        i = round((x - pt[0]) / (3 * self.HEXAGON_SIDE_LENGTH) + (y - pt[1]) / (2 * self.HEXAGON_HALF_HEIGHT))
        j = round((x - pt[0]) / (3 * self.HEXAGON_SIDE_LENGTH) - (y - pt[1]) / (2 * self.HEXAGON_HALF_HEIGHT))
        return i, j
    
    def over_bound(self, pos):
        """
        检测位置是否越界
        
        :param pos: 位置
        :return: True表示越界
        """
        if pos[0] >= self.column or pos[1] >= self.column or pos[0] < 0 or pos[1] < 0:
            return True
        return False
    
    def colorize(self, player, pos):
        """
        为对应格子着色
        
        :param player: 玩家
        :param pos: 位置
        """
        i, j = pos
        pt = ((3 / 2 * self.HEXAGON_SIDE_LENGTH) * (i + j), self.height / 2 + self.HEXAGON_HALF_HEIGHT * (i - j))
        piece = graphics.Polygon(graphics.Point(pt[0], pt[1]),
                                 graphics.Point(pt[0] + self.HEXAGON_SIDE_LENGTH / 2, pt[1] + self.HEXAGON_HALF_HEIGHT),
                                 graphics.Point(pt[0] + 3 * self.HEXAGON_SIDE_LENGTH / 2,
                                                pt[1] + self.HEXAGON_HALF_HEIGHT),
                                 graphics.Point(pt[0] + 2 * self.HEXAGON_SIDE_LENGTH, pt[1]),
                                 graphics.Point(pt[0] + 3 * self.HEXAGON_SIDE_LENGTH / 2,
                                                pt[1] - self.HEXAGON_HALF_HEIGHT),
                                 graphics.Point(pt[0] + self.HEXAGON_SIDE_LENGTH / 2, pt[1] - self.HEXAGON_HALF_HEIGHT))
        piece.setFill(self.COLOR[player])
        piece.draw(self.win)
    
    def show_message(self, message):
        """
        窗口中显示信息
        
        :param message: 要显示的信息
        """
        graphics.Text(graphics.Point(100, 100), message).draw(self.win)
    
    def __init__(self, column):
        """
        初始化棋盘
        
        :param column: 棋盘阶数
        """
        self.column = column
        self.HEXAGON_SIDE_LENGTH = 40
        self.HEXAGON_HALF_HEIGHT = self.HEXAGON_SIDE_LENGTH * (sqrt(3) / 2)  # half height of a hexagon
        
        self.width = (3 * column - 1) * self.HEXAGON_SIDE_LENGTH  # the width of the window
        self.height = 2 * self.HEXAGON_SIDE_LENGTH * column  # the position of the next point determined by the AI
        self.win = graphics.GraphWin("HexGame", self.width, self.height)
        
        self.win.setBackground("white")
        pt = (0, self.height / 2)
        for i in range(column):
            for j in range(column):
                self.draw_hexagon(pt[0] + (3 / 2 * self.HEXAGON_SIDE_LENGTH) * (i + j),
                                  pt[1] + self.HEXAGON_HALF_HEIGHT * (i - j))
        for i in range(column):
            self.draw_line_red(i)
            self.draw_line_blue(i)
    
    def __del__(self):
        self.win.close()