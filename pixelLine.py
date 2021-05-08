
class pLine():
    def __init__(self, p1, p2, c1, c2):
        self.p1 = p1
        self.p2 = p2
        self.c1 = c1
        self.c2 = c2
        self.createLine()
    
    def createLine(self):
        x1 = min(self.p1[0], self.p2[0])
        x2 = max(self.p1[0], self.p2[0])
        y1 = min(self.p1[1], self.p2[1])
        y2 = max(self.p1[1], self.p2[1])
        dx = x2-x1
        dy = y2-y1
        dc = ()
        self.points = []
        for x in range(dx+1):
            self.points.append((x, x*dy/dx))

    def draw(self, win):
        pass