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
        return (self.x, self.y)

class ai(entity):
    def __init__(self):
        entity.__init__(self)

    def smart_move(self):
        #not very smart
        y = random.randint(-1, 1)
        if self.y + y < 0:
            return
        self.move_vert(y)



def init_colors():
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)


def main(scr):

    init_colors()

    curses.curs_set(0)

    # set up
    b1 = entity()
    b1.name = 'p1'

    b2 = ai()
    b2.name = 'p2'
    b2.x = 20

    ball = entity()
    ball.name = 'ball'

    entity_list = [b1, b2, ball]

    # main loop
    while True:

        scr.clear()
        render(scr, entity_list[0])
        render(scr, entity_list[1])

        # update the ai
        entity_list[1].smart_move()
        # move ball

        # allow the person to move
        ch = scr.getch()
        #print ch
        if ch == 259: entity_list[0].move_vert(-1)
        if ch == 258: entity_list[0].move_vert(1)

        # show it on the screen!
        
        # frame rate, duh
        scr.refresh()
        time.sleep(0.01)



def render(scr, item):
    scr.attrset(curses.color_pair(1))
    #try:
    scr.addch(item.y, item.x, ' ')
    #except Exception, e: print e
    #print 'drawing %s at %d,%d' % (item.name, item.x, item.y)


if __name__=="__main__":
    curses.wrapper(main)
