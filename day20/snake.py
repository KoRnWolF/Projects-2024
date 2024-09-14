from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.last_segment_num = len(self.segments) - 1

    def create_snake(self):

        for position in STARTING_POS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """moves the snake segments, from last to next and then next"""
        for seg_idx in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_idx - 1].xcor()
            new_y = self.segments[seg_idx - 1].ycor()
            self.segments[seg_idx].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def add_segments(self):
        """Rough code to add segments"""
        last_segment = self.segments[self.last_segment_num]
        last_segment_pos = last_segment.pos()
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(last_segment_pos)
        self.segments.append(new_segment)



