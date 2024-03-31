from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.readfile())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.write(f"Your score: {self.score}")
        self.score = 0
        self.writefile()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    #    def game_over(self):
    #        self.goto(0, 0)
    #        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def readfile(self):
        with open("data.txt", mode="r") as file:
            readscore = file.read()
            return readscore

    def writefile(self):
        with open("data.txt", mode="w", ) as f:
            f.write(str(self.high_score))
