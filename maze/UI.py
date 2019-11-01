from maze.solve import *
from maze.Generator import *

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 130, bold=True)
font2 = pygame.font.SysFont(None, 40)
font3 = pygame.font.SysFont(None, 30)
font4 = pygame.font.SysFont(None, 22)

color_inactive = pygame.Color('paleturquoise3')
color_active = pygame.Color('paleturquoise4')
button_color = pygame.Color('darkgoldenrod1')
button_color2 = pygame.Color('darkslategray4')

def main():
    done = False

    text = font.render("Maz3rs", True, (56,142,142))
    text2 = font2.render("3D Maze Generator & Solver", True, (255,165,0))
    input_box = pygame.Rect(210, 270, 200, 20)
    color = color_inactive
    active = False
    textInside = ''

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        textInside = ''
                    elif event.key == pygame.K_BACKSPACE:
                        textInside = text[:-1]
                    else:
                        textInside += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
            color = color_active if active else color_inactive

        screen.fill((255,222,173))
        screen.blit(text,(120, 100))
        screen.blit(text2,(115, 190))
        txt_surface = font3.render(textInside, True, color)

        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width

        pygame.draw.rect(screen, color, input_box, 2)
        text_button2 = font4.render("Enter Maze Dimesion :", True, (82,139,139))
        screen.blit(text_button2, (230, 250))

        mouse = pygame.mouse.get_pos()

        button1(textInside)
        button2(textInside)

        pygame.display.flip()
        clock.tick(60)


def button1(text):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 120 + 150 > mouse[0] > 120 and 320 + 100 > mouse[1] > 320:
        pygame.draw.rect(screen, button_color2, (120, 320, 150, 100), 1)
        text_button = font2.render("Generate", True, button_color2)
        screen.blit(text_button, (130, 340))
        text_button2 = font2.render("A*", True, button_color2)
        screen.blit(text_button2, (180, 370))
        if click[0] == 1:
            pygame.quit()
            dimension = int(text)
            maze , n = generate(dimension)
            print(n)
            solve_astar(maze, dimension)
            exit()

    else:
        pygame.draw.rect(screen, button_color, (120, 320, 150, 100), 1)
        text_button = font2.render("Generate", True, button_color)
        screen.blit(text_button, (130, 340))
        text_button2 = font2.render("A*", True, button_color)
        screen.blit(text_button2, (180, 370))


def button2(text):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 360 + 150 > mouse[0] > 360 and 320 + 100 > mouse[1] > 320:
      pygame.draw.rect(screen, button_color2, (360, 320, 150, 100), 1)
      text_button = font2.render("Generate", True, button_color2)
      screen.blit(text_button, (370, 340))
      text_button2 = font2.render("BFS", True, button_color2)
      screen.blit(text_button2, (405, 370))
      if click[0] == 1:
          pygame.quit()
          dimension = int(text)
          maze , n= generate(dimension)
          # print(n)
          solve_BFS(maze, dimension)
          # print(maze)
          # visualize(n, maze, call())

          exit()
    else:
      pygame.draw.rect(screen, button_color, (360, 320, 150, 100), 1)
      text_button = font2.render("Generate", True, button_color)
      screen.blit(text_button, (370, 340))
      text_button2 = font2.render("BFS", True, button_color)
      screen.blit(text_button2, (405, 370))
