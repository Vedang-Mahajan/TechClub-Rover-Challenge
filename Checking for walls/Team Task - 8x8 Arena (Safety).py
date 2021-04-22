import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption("8x8 Arena")

init_x = 717
init_y = 617

# Image ID to be placed in each cell
arena_map = [[0, 1, 0, 1, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 1, 1, 1, 0],
             [0, 1, 0, 1, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 1, 1],
             [0, 0, 0, 0, 1, 0, 1, 1],
             [1, 1, 1, 0, 1, 0, 1, 1],
             [0, 1, 0, 0, 0, 0, 0, 3]]

# Importing the required images
bot_img_temp = pygame.image.load("Bot Icon.png")
empty = pygame.image.load("0.png")
closed = pygame.image.load("5.png")
target = pygame.image.load("3.png")
# pixel = pygame.image.load("1-pixel.png")

# Transforming images as required
bot_img = pygame.transform.scale(bot_img_temp, (70, 70))

# 'event' variable to
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
    if init_x > 100 and init_y > 100 and init_x < 700 and init_y < 700:
        top_colour = screen.get_at(((init_x + 33), (init_y - 67)))
        bottom_colour = screen.get_at(((init_x + 33), (init_y + 133)))
        left_colour = screen.get_at(((init_x - 67), (init_y + 33)))
        right_colour = screen.get_at(((init_x + 133), (init_y + 33)))
        print("Top:", top_colour, "Bottom:", bottom_colour,
              "Left:", left_colour, "Right:", right_colour)
    elif init_x > 0 and init_y > 0 and init_x < 100 and init_y < 100:
        bottom_colour = screen.get_at(((init_x + 33), (init_y + 133)))
        right_colour = screen.get_at(((init_x + 133), (init_y + 33)))
        print("Right:", right_colour, "Bottom:", bottom_colour)
    elif init_x > 100 and init_x < 700 and init_y > 0 and init_y < 100:
        left_colour = screen.get_at(((init_x - 67), (init_y + 33)))
        right_colour = screen.get_at(((init_x + 133), (init_y + 33)))
        bottom_colour = screen.get_at(((init_x + 33), (init_y + 133)))
        print("Left:", left_colour, "Right:",
              right_colour, "Bottom:", bottom_colour)
    elif init_x > 700 and init_y > 0 and init_x < 800 and init_y < 100:
        bottom_colour = screen.get_at(((init_x + 33), (init_y + 133)))
        left_colour = screen.get_at(((init_x - 67), (init_y + 33)))
        print("Left:", left_colour, "Bottom:", bottom_colour)
    elif init_x > 0 and init_y > 100 and init_x < 100 and init_y < 700:
        top_colour = screen.get_at(((init_x + 33), (init_y - 67)))
        bottom_colour = screen.get_at(((init_x + 33), (init_y + 133)))
        right_colour = screen.get_at(((init_x + 133), (init_y + 33)))
        print("Top:", top_colour, "Bottom:",
              bottom_colour, "Right:", right_colour)
    elif init_x > 0 and init_x < 100 and init_y > 700 and init_y < 800:
        top_colour = screen.get_at(((init_x + 33), (init_y - 67)))
        right_colour = screen.get_at(((init_x + 133), (init_y + 33)))
        print("Right:", right_colour, "Top:", top_colour)
    elif init_x > 700 and init_x < 800 and init_y > 700 and init_y < 800:
        top_colour = screen.get_at(((init_x + 33), (init_y - 67)))
        left_colour = screen.get_at(((init_x - 67), (init_y + 33)))
        print("Top:", top_colour, "Left:", left_colour)
    elif init_x > 100 and init_x < 700 and init_y > 700 and init_y < 800:
        top_colour = screen.get_at(((init_x + 33), (init_y - 67)))
        left_colour = screen.get_at(((init_x - 67), (init_y + 33)))
        right_colour = screen.get_at(((init_x + 133), (init_y + 33)))
        print("Top:", top_colour, "Right:", right_colour, "Left:", left_colour)
    elif init_x > 700 and init_x < 800 and init_y > 100 and init_y < 700:
        top_colour = screen.get_at(((init_x + 33), (init_y - 67)))
        bottom_colour = screen.get_at(((init_x + 33), (init_y + 133)))
        left_colour = screen.get_at(((init_x - 67), (init_y + 33)))
        print("Top:", top_colour, "Bottom:",
              bottom_colour, "Left:", left_colour)
    else:
        print("Sorry, unidentified area :(")


createMap()

screen.blit(bot_img, (init_x, init_y))

pygame.display.update()

checkCell()

while True:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event = "quit"
            pygame.quit()
            break
    if event == "quit":
        break
