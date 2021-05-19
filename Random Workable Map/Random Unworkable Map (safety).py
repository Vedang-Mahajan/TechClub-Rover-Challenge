"""

PSEUDO CODE:

Set the start cell
Set the target cell

mapFound = False

def CreateMap():
    Generate the arena with random open and close blocks

Loop until mapFound == True
    Check the cells around the bot using the '8x8 Arena' code.

    Add that cell co-ordinate to the map_cells dictionary with the value 1 if that cell is open or 0 if closed. (This will be done for all the possible cells that the bot can reach)

    If current_cell in map_cells:
        reroute to other cell if open
    Else:
        Go back

    If Cell co-ordinates and blocked/closed data for all the cells == True:
        If there are blocks adjacent to the blocks tracing from the start to target cell:
            mapFound = True
            Random Workable Map Generated!
            break
    Else:
        There is no path available for the bot to travel
        CreateMap()
        break

"""

"""
while init_x != target_x and init_y != target_y and mapFound == False:
    openCell = checkCell()
    for a in openCell:
        if ((str(a[0]) + " " + str(a[1]))) not in map_cells:
            for i in openCell:
                map_cells[str(i[0]) + " " + str(i[1])] = 0
                init_x = i[0]
                init_y = i[1]
            print(map_cells)
"""

# from time import sleep

import math
import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Random Workable Map")

# Start cell
init_x = 17
init_y = 17

target_x = 717
target_y = 717

# Whether the map has been found
mapFound = False

instances = []

# Importing the required images
bot_img_temp = pygame.image.load("Bot_Icon.png")
empty = pygame.image.load("0.png")
closed = pygame.image.load("5.png")
target = pygame.image.load("3.png")
pixel = pygame.image.load("1-dot.png")

# Transforming images as required
bot_img = pygame.transform.scale(bot_img_temp, (70, 70))

arena_map = []
row_list = []

map_cells = {}

map_cells[(str(init_x) + " " + str(init_y))] = 0
map_cells[(str(target_x) + " " + str(target_y))] = 3

for i in range(8):
    row_list = []
    for j in range(8):
        row_list.append(random.randint(0, 1))
    arena_map.append(row_list)

arena_map[0][0] = 0
arena_map[(math.trunc((target_x-17)/100))][(math.trunc((target_y-17)/100))] = 3

event = ""

map_elements = {
    0: empty,
    1: closed,
    3: target
}


def createMap():
    # Co-ordinates for displaying the images in specific cells.
    x = 0
    y = 0

    for a in arena_map:
        y = 0

        for b in a:
            screen.blit(map_elements[b], (x, y))
            y += 100
        x += 100


def checkCell():
    openCells = []

    if init_x > 100 and init_y > 100 and init_x < 700 and init_y < 700:
        top_colour = screen.get_at(((init_x + 33), (init_y - 67)))
        bottom_colour = screen.get_at(((init_x + 33), (init_y + 133)))
        left_colour = screen.get_at(((init_x - 67), (init_y + 33)))
        right_colour = screen.get_at(((init_x + 133), (init_y + 33)))

        if top_colour == (255, 255, 255, 255):
            openCells.append([(init_x), (init_y - 100)])
        if right_colour == (255, 255, 255, 255):
            openCells.append([(init_x + 100), (init_y)])
        if bottom_colour == (255, 255, 255, 255):
            openCells.append([(init_x), (init_y + 100)])
        if left_colour == (255, 255, 255, 255):
            openCells.append([(init_x - 100), (init_y)])

    elif init_x > 0 and init_y > 0 and init_x < 100 and init_y < 100:
        bottom_colour = screen.get_at(((init_x + 33), (init_y + 133)))
        right_colour = screen.get_at(((init_x + 133), (init_y + 33)))

        if right_colour == (255, 255, 255, 255):
            openCells.append([(init_x + 100), (init_y)])
        if bottom_colour == (255, 255, 255, 255):
            openCells.append([(init_x), (init_y + 100)])

    elif init_x > 100 and init_x < 700 and init_y > 0 and init_y < 100:
        left_colour = screen.get_at(((init_x - 67), (init_y + 33)))
        right_colour = screen.get_at(((init_x + 133), (init_y + 33)))
        bottom_colour = screen.get_at(((init_x + 33), (init_y + 133)))

        if right_colour == (255, 255, 255, 255):
            openCells.append([(init_x + 100), (init_y)])
        if bottom_colour == (255, 255, 255, 255):
            openCells.append([(init_x), (init_y + 100)])
        if left_colour == (255, 255, 255, 255):
            openCells.append([(init_x - 100), (init_y)])

    elif init_x > 700 and init_y > 0 and init_x < 800 and init_y < 100:
        bottom_colour = screen.get_at(((init_x + 33), (init_y + 133)))
        left_colour = screen.get_at(((init_x - 67), (init_y + 33)))

        if bottom_colour == (255, 255, 255, 255):
            openCells.append([(init_x), (init_y + 100)])
        if left_colour == (255, 255, 255, 255):
            openCells.append([(init_x - 100), (init_y)])

    elif init_x > 0 and init_y > 100 and init_x < 100 and init_y < 700:
        top_colour = screen.get_at(((init_x + 33), (init_y - 67)))
        bottom_colour = screen.get_at(((init_x + 33), (init_y + 133)))
        right_colour = screen.get_at(((init_x + 133), (init_y + 33)))

        if top_colour == (255, 255, 255, 255):
            openCells.append([(init_x), (init_y - 100)])
        if right_colour == (255, 255, 255, 255):
            openCells.append([(init_x + 100), (init_y)])
        if bottom_colour == (255, 255, 255, 255):
            openCells.append([(init_x), (init_y + 100)])

    elif init_x > 0 and init_x < 100 and init_y > 700 and init_y < 800:
        top_colour = screen.get_at(((init_x + 33), (init_y - 67)))
        right_colour = screen.get_at(((init_x + 133), (init_y + 33)))

        if top_colour == (255, 255, 255, 255):
            openCells.append([(init_x), (init_y - 100)])
        if right_colour == (255, 255, 255, 255):
            openCells.append([(init_x + 100), (init_y)])

    elif init_x > 700 and init_x < 800 and init_y > 700 and init_y < 800:
        top_colour = screen.get_at(((init_x + 33), (init_y - 67)))
        left_colour = screen.get_at(((init_x - 67), (init_y + 33)))

        if top_colour == (255, 255, 255, 255):
            openCells.append([(init_x), (init_y - 100)])
        if left_colour == (255, 255, 255, 255):
            openCells.append([(init_x - 100), (init_y)])

    elif init_x > 100 and init_x < 700 and init_y > 700 and init_y < 800:
        top_colour = screen.get_at(((init_x + 33), (init_y - 67)))
        left_colour = screen.get_at(((init_x - 67), (init_y + 33)))
        right_colour = screen.get_at(((init_x + 133), (init_y + 33)))

        if top_colour == (255, 255, 255, 255):
            openCells.append([(init_x), (init_y - 100)])
        if right_colour == (255, 255, 255, 255):
            openCells.append([(init_x + 100), (init_y)])
        if left_colour == (255, 255, 255, 255):
            openCells.append([(init_x - 100), (init_y)])

    elif init_x > 700 and init_x < 800 and init_y > 100 and init_y < 700:
        top_colour = screen.get_at(((init_x + 33), (init_y - 67)))
        bottom_colour = screen.get_at(((init_x + 33), (init_y + 133)))
        left_colour = screen.get_at(((init_x - 67), (init_y + 33)))

        if top_colour == (255, 255, 255, 255):
            openCells.append([(init_x), (init_y - 100)])
        if bottom_colour == (255, 255, 255, 255):
            openCells.append([(init_x), (init_y + 100)])
        if left_colour == (255, 255, 255, 255):
            openCells.append([(init_x - 100), (init_y)])

    else:
        raise ValueError("Unidentified area")

    return openCells


createMap()

pygame.display.update()

while init_x != target_x and init_y != target_y and mapFound == False:
    openCell = checkCell()
    # instances = list(openCell)
    for a in openCell:
        if len(openCell) == 1:
            if ((str(a[0]) + " " + str(a[1]))) not in map_cells:
                map_cells[str(a[0]) + " " + str(a[1])] = 0
                init_x = a[0]
                init_y = a[1]
        else:
            instances.append(
                [(str(init_x) + " " + str(init_y)), len(openCell)])
            if ((str(a[0]) + " " + str(a[1]))) not in map_cells:
                map_cells[str(a[0]) + " " + str(a[1])] = 0
                init_x = a[0]
                init_y = a[1]
        print(map_cells)

print("")
print(arena_map.index(arena_map[3]))
print("")

print(map_cells)

while True:
    pygame.display.update()

    screen.blit(bot_img, (init_x, init_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event = "quit"
            pygame.quit()
            break
    if event == "quit":
        break
