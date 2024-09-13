class CreateT:
    def __init__(self):
        self.t_color = ""
        self.t_posx = 0
        self.t_posy = 0
        self.shape = "turtle"


    def maket(self, turt, t_color, t_posx, t_posy):

            self.t_color = "red"
            self.t_posx = -225
            self.t_posy = 0

        turt.color(t_color)
        turt.speed("slow")
        turt.penup()
        turt.setpos(t_posx, t_posy)
