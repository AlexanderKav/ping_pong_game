from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", move=False, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", move=False, align="center", font=("Courier", 80, "normal"))


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", move=False, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", move=False, align="center", font=("Courier", 80, "normal"))



    def l_higher_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_higher_score(self):
        self.r_score += 1
        self.update_scoreboard()