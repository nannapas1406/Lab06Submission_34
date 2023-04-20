class InputBox:
    def __init__(self, x, y, w, h, IsAlpha, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.alpha = IsAlpha

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.alpha == True:
                        self.text += event.unicode
                    else:
                        if chr(event.key).isnumeric():
                            self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

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
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))

run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,350,170,50,(176,224,230)) # สร้าง Object จากคลาส Button ขึ้นมา

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 26)

input_box1 = InputBox(250, 90, 140, 26, True) # สร้าง InputBox1
input_box2 = InputBox(250, 190, 140, 26, True) # สร้าง InputBox2
input_box3 = InputBox(250, 280, 140, 26, False) # สร้าง InputBox2
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย
run = True

font = pg.font.Font('freesansbold.ttf', 26) # font and fontsize
text1 = font.render('Firstname : ', True, 'white', (0,0,0)) # (text,is smooth?,letter color,background color)
textRect1 = text1.get_rect() # text size
textRect1.center = (win_x -690, win_y -375)

text2 = font.render('Lastname : ', True, 'white', (0,0,0)) # (text,is smooth?,letter color,background color)
textRect2 = text2.get_rect() # text size
textRect2.center = (win_x -690, win_y -275)

text3 = font.render('Age : ', True, 'white', (0,0,0)) # (text,is smooth?,letter color,background color)
textRect3 = text3.get_rect() # text size
textRect3.center = (win_x -730, win_y -185)

text4 = font.render('Submit', True, 'black', (176,224,230))
textRect4 = text4.get_rect() # text size
textRect4.center = (win_x -700, win_y -100)

text = font.render('', True, 'black', (255,255,255))
textRect = text.get_rect() # text size
textRect.center = (win_x -600, win_y -100)

while run:
    screen.fill((255, 255, 255))
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text, textRect)

    if btn.isMouseOn() and btn.isMousePressed():
        text = font.render('Hello ' + input_box1.text + ' ' + input_box2.text + '!' + ' You are ' + input_box3.text  + ' years old.', True, 'black', (255,255,255))

    btn.draw(screen)

    screen.blit(text4, textRect4)


    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False

    pg.time.delay(1)
    pg.display.update()