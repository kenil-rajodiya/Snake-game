from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score=0
        with open("data.txt") as f:
            self.high_score = int(f.read())
        self.hideturtle()
        self.goto(0,280)
        self.color("gold")

    def update(self):
        self.clear()
        self.write(f"Score {self.score} High Score: {self.high_score}",move=False,align="center",font=("sans-serif",15,"normal"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over",move=False,align="center",font=("Arial",15,"normal"))


    def reset(self):
        if self.high_score<self.score:
            self.high_score=self.score
            with open("data.txt",mode="w") as file:
                file.write(str(self.high_score))

        self.score=0
        self.update()


    def increase_score(self):
        self.score+=1
        self.update()
