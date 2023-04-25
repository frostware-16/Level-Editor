import pygame
import time
import math
import random
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()


pygame.init()
screen = pygame.display.set_mode((800, 800))
running = True
fps = 60
walls = []
bgs = []
goals = []
Enmeies = []
coins = []
code = ""
lineMode = 1
ShowModeLine = 0
ShowModebg = 0
class Level:
    def __init__(self,count,x,y):
        self.count =  simpledialog.askstring(title="enter",prompt="level number")
        self.startx = simpledialog.askstring(title="enter",prompt="startx")
        self.starty = simpledialog.askstring(title="enter",prompt="starty")
        self.enemylist = []
        self.goallist = []
        self.WallList = []

class Enemy:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.radius = 4.5*4
        self.speed = simpledialog.askstring(title="enter",prompt="speed")
        self.dir = simpledialog.askstring(title="enter",prompt="direction")
        self.dist = simpledialog.askstring(title="enter",prompt="distance")

    def render(self):
        pygame.draw.rect(screen, (255,0,0), (self.x*4,self.y*4,35,35))
class bg:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def render(self):
        pygame.draw.rect(screen, (102, 140, 255), (self.x*4,self.y*4,40,40))

class coin:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def render(self):
        pygame.draw.rect(screen, (255,255,0), (self.x*4,self.y*4,40,40))
class wall:
    def __init__(self,x,y,dirc):
        self.x = x
        self.y = y
        self.dirc = dirc

    def render(self):
        if self.dirc == 1:pygame.draw.rect(screen, (0,0,0), (self.x*4,self.y*4,1,10*4))
        if self.dirc == 2:pygame.draw.rect(screen, (0,0,0), (self.x*4,self.y*4,10*4,1))

class goal:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def render(self):
        pygame.draw.rect(screen, (153, 255, 102), (self.x*4,self.y*4,40,40))

def datatocode():
    global code
    code += "Level level" + str(l.count) +" = Level("
    code += str(l.count) + ","
    code += str(l.startx) + ","
    code += str(l.starty) + ","
    code += "{" 
    #Enemy(int x, int y, float speed, int radius, int direction, int distance)
    for e in Enmeies:
        code += "Enemy("
        code += str(e.x+6) + ","
        code += str(e.y+6) + ","
        code += str(e.speed) + ","
        code += str(4.5) + ","
        code += str(e.dir) + ","
        code += str(e.dist)
        if e == Enmeies[-1]:
            code += ")"
        else:
            code += ") ,"
    code += "}" + ","
    code += "{" 
    for g in goals:
        code += "Goal("
        code += str(g.x+1) + ","
        code += str(g.y+1) + ","
        code += str(10) + ","
        code += str(10) + ","
        code += str("true") + ","
        code += str(l.count)
        if g == goals[-1]:
            code += ")"
        else:
            code += ") ,"

    code += "}" + ","
    code += "{"
    for w in walls:
        code += "Wall("
        code += str(w.x) + ","
        code += str(w.y) + ","
        code += str(11) + ","
        code += str(w.dirc)
        if w == walls[-1]:
            code += ")"
        else:
            code += ") ,"

    code += "}" + ","
    code += "{" 

    for b in bgs:
        code += "Background("
        code += str(b.x+1) + ","
        code += str(b.y+1) + ","
        code += str(10) + ","
        code += str(10)
        if b == bgs[-1]:
            code += ")"
        else:
            code += ") ,"
    code += "}" + ","
    code += "{" 
    for c in coins:
        code += "Coin("
        code += str(c.x+6) + ","
        code += str(c.y+6)
        if c == coins[-1]:
            code += ")"
        else:
            code += ") ,"
    code += "}" +")" + ";"

# Level level1 = Level(1,200,200,{},{},{wall(84,133,25,1)},{})

l = Level(1,200,200)

print(code)
edown = False
cdown = False
ddown = False
vdown = False
bdown = False
gdown = False
adown = False
ldown = False
pdown = False

while running:
        x, y = pygame.mouse.get_pos()
        x -= 40
        y -= 40
        x = round(x/40)*40+20-1
        y = round(y/40)*40+20-1
        screen.fill((100,100,100))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_b:
                        bdown = False
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        x = x // 4
                        y = y // 4
                        for w in walls:
                            print(w.x , x ,w.y , y)
                            if w.x == x and w.y == y:
                                walls.remove(w)

                        for w in bgs:
                            print(w.x , x ,w.y , y)
                            if w.x == x and w.y == y:
                                bgs.remove(w)
                        
                        for w in goals:
                            print(w.x , x ,w.y , y)
                            if w.x == x and w.y == y:
                                goals.remove(w)

                        for c in coins:
                            print(c.x , x ,c.y , y)
                            if c.x == x and c.y == y:
                                coins.remove(c) 
                        
                        for c in Enmeies:
                            print(c.x , x ,c.y , y)
                            if c.x == x and c.y == y:
                                Enmeies.remove(c) 
                    if event.key == pygame.K_c:
                        if ShowModeLine == 0: ShowModeLine = 1
                        else: ShowModeLine = 0
                        print(ShowModeLine)

                    if event.key == pygame.K_d:
                        if ShowModebg == 0: ShowModebg = 1
                        else: ShowModebg = 0

                    if event.key == pygame.K_v:
                        
                        w = wall(x//4,y//4,lineMode)
                        walls.append(w)
                    if event.key == pygame.K_b:
                        bdown = True
                        
                        

                    if event.key == pygame.K_g:
                        
                        g = goal(x//4,y//4)
                        goals.append(g)

                    if event.key == pygame.K_a:
                        
                        e = Enemy(x//4,y//4)
                        Enmeies.append(e)
                    if event.key == pygame.K_k:
                        c = coin(x//4,y//4)
                        coins.append(c)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        if lineMode == 1: lineMode = 2
                        else: lineMode = 1

                    if event.key == pygame.K_p:
                        print(code)

        
        for b in bgs:
            b.render()
        
        for g in goals:
            g.render()
        
        for e in Enmeies:
            e.render()
        
        for w in walls:
            w.render()
        
        for c in coins:
            c.render()
        if bdown:
            for b in bgs:
                if b.x == x//4 and b.y == y//4:
                    bgs.remove(b)
            b = bg(x//4,y//4)
            bgs.append(b)
        if ShowModeLine:
            
            if lineMode == 2:
                pygame.draw.rect(screen, (0,200,0), (x,y,40,1))
            if lineMode == 1:
                pygame.draw.rect(screen, (0,200,0), (x,y,1,40))

        if ShowModebg:
            
            pygame.draw.rect(screen, (0,255,0), (x,y,40,40))

        code = ""
        datatocode()
        time.sleep(1/fps)
        pygame.display.update()