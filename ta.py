'''

cave cliff river

look
walk forward/backward
turn left/right/around
jump
pick up / grab
push
TODO: "get turnt" mode
'''

from random import choice as ch

terrain = [x for x in '~?*X ']
dirs = [x for x in 'NESW']
direction = 'N'
inventory = []
state = []

def describe():
    print 'You are facing %s.'%direction

def turn(cw):
    global direction
    direction = dirs[(dirs.index(direction)+cw)%4]

def show_map():
    m = [[ch(terrain) for j in xrange(5)] for i in xrange(3)]
    for i in xrange(3):
        for j in xrange(5):
            print m[i][j],
        print ''
while True:
    entry = raw_input('>> ')
    if 'help' in entry:
        print 'look turn map'
    if 'look' in entry:
        describe()
    if 'turn' in entry:
        if 'left' in entry:
            turn(3)
        elif 'right' in entry:
            turn(1)
        elif 'around' in entry:
            turn(2)
    if 'map' in entry:
        show_map()
