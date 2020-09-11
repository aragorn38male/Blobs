class Blob:
    
    def __init__(self,x,y):
        self.n=0
        self.x=x
        self.y=y
        self.r = random(10,50)
        self.vel=PVector.random2D()
        self.vel.mult(random(self.r/6,self.r/6))
        self.pos = PVector (self.x , self.y)
        
    def update(self):
        self.pos.add(self.vel)
        if self.pos.x>width or self.pos.x<0:
            self.vel.x*=-1
        if self.pos.y>height or self.pos.y<0:
            self.vel.y*=-1