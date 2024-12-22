from ctypes.wintypes import DWORD
from idlelib.zoomheight import WmInfoGatheringError
from turtle import Screen,Turtle
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    segments = []
    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    # head is segments[0]
    def __init__(self):
        for position in self.starting_positions:
            self.add_segment(position)
        self.segments[0].color("pink")
        self.segments[0].shape("square")

    def add_segment(self,position):
        t1 = Turtle("square")
        t1.penup()
        t1.color("white")
        t1.goto(position)
        self.segments.append(t1)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.__init__()