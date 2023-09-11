from turtle import Turtle, Screen
screen = Screen()
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()

    def bounce_y(self):
        self.ymove *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9



   # def hittop_of_wall(self):
    #    new_x = self.xcor() + 10
     #   #new_x = self.xcor() - 10
      #  new_y = self.ycor() - 10
       # self.goto(new_x, new_y)

    #def hitbottom_of_wall(self):
     #   new_x = self.xcor() - 10
      #  new_y = self.ycor() + 10
       # self.goto(new_x, new_y)

#my solution
    #def move(self):
     #   y = 0
      #  for x in range(1, 370):
       #     y = y+0.78
        #    self.goto(x, y)
         #   screen.update()





