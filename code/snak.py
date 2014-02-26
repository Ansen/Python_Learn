# snakegame

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import random


class Snake:
    def __init__(self):
        self.length = 4
        self.posArray = [(3,0),(2,0),(1,0),(0,0)]
        self.isDead = 0

class Food:
    def __init__(self):
        self.isExist = 0
        self.pos = (0,0)


class SnakeGame(QWidget):

    def __init__(self):
        super(SnakeGame, self).__init__()
        self.timer = QTimer(self)
        #self.connect(timer, SIGNAL("timeout()"),self,SLOT("update()"))
        self.timer.timeout.connect(self.update)
        self.initGame()
        self.initUI()

    def initUI(self):

        #self.setGeometry(300, 300, 500, 300)
        self.setMaximumSize(500,330)
        self.setMinimumSize(500,330)
        self.show()

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)

        if self.isStart == -1:
            self.pause(event, qp)
        elif self.isStart == 0:
            self.readyGame(event, qp)
        elif self.isStart == 1:
            self.proceedGame(event, qp)
        else:
            self.overGame(event, qp)

        qp.end()

    def keyPressEvent(self, event):
        key = event.key()
        if self.isStart == 1:
            if key == Qt.Key_Left and self.tag != 'Right':
                self.xch = -1
                self.ych = 0
                self.tag = 'Left'
            if key == Qt.Key_Right and self.tag != 'Left':
                self.xch = 1
                self.ych = 0
                self.tag = 'Right'
            if key == Qt.Key_Down and self.tag != 'Up':
                self.ych = 1
                self.xch = 0
                self.tag = 'Down'
            if key == Qt.Key_Up and self.tag != 'Down':
                self.ych = -1
                self.xch = 0
                self.tag = 'Up'
        if key == Qt.Key_Space:
            if self.isStart == 0:
                self.isStart = 1
            elif self.isStart == 2:
                self.initGame()
                self.isStart = 0
            else:
                self.isStart = -self.isStart

    def drawSquare(self, qp, xx, yy):
        qp.drawRect(xx*10, yy*10, 10, 10)
    def drawBlackSquare(self, qp, xx, yy):
        qp.setBrush(QColor(0,0,0))
        qp.drawRect(xx*10,yy*10,10,10)

    def drawSnake(self,qp):
        for a in self.snake.posArray:
            xx = a[0]
            yy = a[1]
            self.drawSquare(qp, xx, yy)

    def moveSnake(self):
        l = len(self.snake.posArray)
        for i in xrange(l-1, 0, -1):
            self.snake.posArray[i] = self.snake.posArray[i-1]
        xx = self.snake.posArray[0][0]
        yy = self.snake.posArray[0][1]
        self.snake.posArray[0] = (xx+self.xch, yy+self.ych)
    #def isDead():

    def produceFood(self):
        if self.food.isExist == 0:
            #random.seed()
            xx = random.randint(0, 49)
            yy = random.randint(0, 29)
            while (xx, yy) in self.snake.posArray:
                xx = random.randint(0, 49)
                yy = random.randint(0, 29)
            self.food.pos = (xx, yy)
            self.food.isExist = 1

    def drawFood(self, qp):
        self.drawBlackSquare(qp, self.food.pos[0], self.food.pos[1])

    def eatFood(self):
        l = len(self.snake.posArray)
        if self.snake.posArray[0] == self.food.pos:
            self.snake.posArray.append(self.snake.posArray[l-1])
            self.food.isExist = 0
            self.score = self.score + self.lvl * 100

    def drawCoverText(self, event, qp, text, color):

        qp.setPen(color)
        qp.setFont(QFont('Decorative', 30))
        qp.drawText(event.rect(), Qt.AlignCenter, text)

    def drawStatusText(self, qp, text, xx, yy):
        qp.setPen(QColor(0,0,0))
        qp.setFont(QFont('Decorative', 15))
        qp.drawText(xx, yy, text)

    def drawStatus(self, qp):
        text1 = 'SCORE: ' + str(self.score)
        self.drawStatusText(qp, text1, 10, 315)
        text2 = 'LVL: ' + str(self.lvl)
        self.drawStatusText(qp, text2, 300, 315)

    def pause(self, event, qp):
        color = QColor(0, 0, 0)
        text = 'Pause'
        self.drawCoverText(event, qp, text, color)

    def overGame(self, event, qp):
        color = QColor(0, 0, 0)
        text = 'Game Over'
        self.drawCoverText(event, qp, text, color)
        self.drawSnake(qp)
        self.drawBorder(qp)
        text1 = 'SCORE: ' + str(self.score)
        self.drawStatusText(qp, text1, 185, 220)
        self.drawFood(qp)
        self.isStart = 2

    def initGame(self):
        self.xch, self.ych = 1,0
        self.tag = 'Right'
        self.isStart = 0
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.lvl = 1
        self.timer.start(240)

    def readyGame(self, event, qp):
        self.drawSnake(qp)
        self.drawBorder(qp)
        text = 'Press Space To Play'
        color = QColor(0, 0, 0)
        self.drawCoverText(event, qp, text, color)

    def checkLiveOrDead(self):
        xx = self.snake.posArray[0][0] + self.xch
        yy = self.snake.posArray[0][1] + self.ych
        if xx < 0 or yy < 0 or xx >49 or yy >29 or (xx, yy) in self.snake.posArray:
            self.snake.isDead = 1

    def checkLvl(self):
        if self.score  >= self.lvl * self.lvl *1000:
            time = 240 - self.lvl * 30
            self.lvl = self.lvl + 1
            if time < 0:
                time = 1
            self.timer.start(time)

    def drawBorder(self, qp):
        qp.setPen(QColor(0,0,0))
        qp.drawRect(0,0,500,300)

    def proceedGame(self, event, qp):
        self.checkLiveOrDead()
        self.checkLvl()
        if self.snake.isDead:
            self.overGame(event, qp)
        else:
            self.drawBorder(qp)
            self.moveSnake()
            self.eatFood()
            self.drawSnake(qp)
            self.produceFood()
            self.drawFood(qp)
            self.drawStatus(qp)

def main():
    app = QApplication(sys.argv)
    ex = SnakeGame()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()