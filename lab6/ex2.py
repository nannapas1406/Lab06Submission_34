class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0,color=(0,0,0)):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
        self.c = color # Color
    def draw(self,screen):
        pg.draw.rect(screen,self.c,(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0, color=(0,0,0)):
        Rectangle.__init__(self, x, y, w, h, color)
    
    def isMouseOn(self):
        x, y = pg.mouse.get_pos()
        if x >= self.x and y >= self.y and x <= self.x + self.w and y <= self.y + self.h:
            return True
        else:
            return False
        
    def isMousePressed(self):
        status = pg.mouse.get_pressed()[0]
        if status == 1: # Check mouse pressed
            return True
        else:
            return False
        
import sys 
import pygame as pg

pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100,(0,0,0)) # สร้าง Object จากคลาส Button ขึ้นมา

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn() and btn.isMousePressed():
        btn.c = (147,112,219)
    elif btn.isMouseOn():
        btn.c = (211,211,211)
    else:
        btn.c = (255,0,0)
    btn.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

        # if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
        #     print("Key D down")
        # if event.type == pg.KEYUP and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
        #     print("Key A up")

        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม W
            print("Key W up")
            btn.y -= 30
        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            print("Key A left")
            btn.x -= 30
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            print("Key S down")
            btn.y += 30
        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            print("Key D right")
            btn.x += 30
    
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False