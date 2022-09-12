class Ufo:
    def __init__(self,x,y,change,img,width,height):
        self.x = x
        self.y = y
        self.change = change
        self.img = img
        self.width = width
        self.height = height
    def check_player_boundary(self):
        if self.x <= 5:
            self.x = 5 
        if self.x >= 731:
            self.x = 731
        if self.y <= 445:
            self.y = 445 
        if self.y >= 540:
            self.y = 540 