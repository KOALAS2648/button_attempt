import pygame as pg
from button import *
import math, os
import logo
pg.init()
WIN, HEI = 1080,800

window = pg.display.set_mode((WIN, HEI))
clicky_button = Button("money_click", ((WIN/2)-25, (HEI/2)-25), (50, 50))
clicky_button_surface = pg.Surface(clicky_button.size)
clicky_button_surface.fill((0,0,0))

power_up_button = Button("power_up", ((WIN/2 )+50, (HEI/2)-25), (50, 50))
power_surface = pg.Surface(power_up_button.size)
power_surface.fill((0,255,255))

test_box = Button("test_box", (power_up_button.coords[0]+25, power_up_button.coords[1]+25), (5,5))
text_box_surface = pg.Surface(test_box.size)
text_box_surface.fill((0,0,0))

logo = logo.Logo(((WIN/2)-25, 50), (25, 25), "pictures/koala.png")
koala_image = pg.image.load(logo.image_path)
koala_image = pg.transform.scale(koala_image, (150,150))
window.blit(koala_image, logo.coords)

money = 0
money_power = 1
upgrade_cost_power = 1.15
upradge_pice = 10 
def calculate_distance(coord1:tuple, coord2:tuple):
    return round(math.sqrt((coord2[0]-coord1[0])**2 + (coord2[1]-coord1[1])**2))

fontSize = 40
font = pg.font.SysFont('Sans serif', fontSize)
def draw_text(text,x,y,color):
  label = font.render(text, True, color)
  window.blit(label, (x,y))
RUN = True
def main():
    global RUN, money_power, money, upradge_pice
    while RUN:
        mouse_pos = pg.mouse.get_pos()
        window.blit(koala_image, logo.coords)
        draw_text(f"money scaler:{money_power}", (WIN/2)-50, (HEI/2)-150, (255,0,0))
        draw_text(f"money:{money}", (WIN/2)-50, (HEI/2)-100, (0,0,255))
        draw_text(f"add money price:{upradge_pice}", (WIN/2)-50, (HEI/2)-50, (0,0,255))
        window.blit(clicky_button_surface, clicky_button.coords)
        window.blit(power_surface, power_up_button.coords)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                RUN = False
                os.system("cls")

            dis_money_add = calculate_distance(mouse_pos, (clicky_button.coords[0]+25, clicky_button.coords[1]+25))
            dis_power_up = calculate_distance(mouse_pos, (power_up_button.coords[0]+25, power_up_button.coords[1]+25))
            keys = pg.key.get_pressed()
            if dis_money_add < clicky_button.size[0]-25 and event.type == pg.MOUSEBUTTONDOWN:
                money += money_power
            if (dis_power_up < power_up_button.size[0]-25 and event.type == pg.MOUSEBUTTONDOWN) and (money-upradge_pice) >= 0:
                money_power += 1
                money -= upradge_pice
                upradge_pice *= upgrade_cost_power
                upradge_pice = round(upradge_pice)

        # pg.display.set_caption("python clicker game")
        pg.display.set_caption(str(upradge_pice))
        
        pg.display.flip()
        window.fill((255, 255, 255))
        window.blit(text_box_surface, test_box.coords)

if __name__ == "__main__": 
    main()