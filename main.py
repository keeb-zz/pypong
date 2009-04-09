import time
import random

import curses.wrapper

class entity:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.name = "entity"

    def move_vert(self, amt):
        if self.y + amt < 0:
            return
        self.y += amt

    def move_hori(self, amt):
        if self.x + amt < 0:
            return
        self.x += amt

    def position(self):
        return [(self.x, self.y), (self.x, self.y-1), (self.x, self.y-2)]

    def render(self, scr):
        scr.attrset(curses.color_pair(1))
        scr.addch(self.y, self.x, ' ')
        scr.addch(self.y-1, self.x, ' ')
        scr.addch(self.y-2, self.x, ' ')


class ai(entity):
    def __init__(self):
        entity.__init__(self)

    def smart_move(self):
        #not very smart
        # completely random
        pass

class ball(entity):
    def __init__(self):
        entity.__init__(self)
        self.direction = 'x'

    def render(self, scr):
        """ override base class """
        scr.attrset(curses.color_pair(2))
        scr.addch(self.y, self.x, ' ')

    def position(self):
        return (self.x, self.y)

    def move(self):
        if self.direction == 'x':
            self.x -= 1
        else:
            self.x += 1

    def collision(self):
        # something hit me!
        if self.direction == 'x':
            self.direction = 'y'
        else:
            self.direction = 'x'


def init_colors():
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)


def check_collisions(ball, paddle1, paddle2):
    ball_pos = ball.position()
    paddle1_pos = paddle1.position()
    paddle2_pos = paddle2.position()
    f = open('tmp1', 'a')
    f.write('%s \n' % str(ball.position()) )
    f.write('%s \n' % str(paddle1.position()) )
    f.write('%s \n' % str(paddle2.position()) )
    f.close()

    if ball_pos in paddle1_pos:
        return True
    if ball_pos in paddle2_pos:
        return True

    return False


def main(scr):

    init_colors()
    curses.curs_set(0) # turn off the cursor
    scr.nodelay(1) # do not block on getch()

    # set up
    b1 = entity()
    b1.name = 'p1'
    b1.y = 5

    b2 = ai()
    b2.name = 'p2'
    b2.x = 20
    b2.y = 5

    b = ball()
    b.name = 'ball'
    b.x = 10
    b.y = 5
    


    # main loop
    while True:
        scr.clear()
        # update the ai
        b2.smart_move()

        # move the ball
        b.move()
        # collision?
        if check_collisions(b, b2, b1):
            # update ball velocity, position
            b.collision()

        b2.render(scr)
        b1.render(scr)
        b.render(scr)
            

        # move ball

        # allow the person to move
        ch = scr.getch()
        if ch == 259: b1.move_vert(-1)
        if ch == 258: b1.move_vert(1)
        

        # frame rate, duh
        scr.refresh()
        time.sleep(0.02)



if __name__=="__main__":
    curses.wrapper(main)
