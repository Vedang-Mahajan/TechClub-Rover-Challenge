import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Arena")

init_x = 17
init_y = 17

# Images to be displayed
map = [
    [3, 5, 1, 4, 1],
    [4, 3, 0, 1, 4],
    [4, 3, 1, 4, 4],
    [2, 4, 1, 4, 4],
    [3, 5, 1, 1, 3]]

# Angles on which the images should be rotated
angles = [[180, 0, -90, -90, 180],
          [0, -90, 90, 180, 0],
          [0, -90, 90, 0, 0],
          [0, 90, 180, 0, 0],
          [0, 0, 0, 90, 0]]

# map_coords = {
#     "17 17": map[0][0],  "17 137": map[0][1], "17 257": map[0][2],   "17 377": map[0][3], "17 497": map[0][4],
#     "137 17": map[1][0], "137 137": map[1][1], "137 257": map[1][2], "137 377": map[1][3], "137 497": map[1][4],
#     "257 17": map[2][0], "257 137": map[2][1], "257 257": map[2][2], "257 377": map[2][3], "257 497": map[2][4],
#     "377 17": map[3][0], "377 137": map[3][1], "377 257": map[3][2], "377 377": map[3][3], "377 497": map[3][4],
#     "497 17": map[4][0], "497 137": map[4][1], "497 257": map[4][2], "497 377": map[4][3], "497 497": map[4][4]
# }

# print(map_coords["257 257"])

# Importing the original bot image
bot_img_old = pygame.image.load("Bot Icon.png")
# arena_old = pygame.image.load("Arena.png")

# Importing the original images
nothing = pygame.image.load("0.png")
left_and_bottom = pygame.image.load("1.png")
bottom = pygame.image.load("2.png")
left_right_bottom = pygame.image.load("3.png")
left_and_right = pygame.image.load("4.png")
all_sides = pygame.image.load("5.png")
left_and_top = pygame.transform.rotate
pixel = pygame.image.load("1-pixel.png")

# Dictionary pointing out numbers to their image
map_elements = {
    0: nothing,
    1: left_and_bottom,
    2: bottom,
    3: left_right_bottom,
    4: left_and_right,
    5: all_sides
}

# New bot image
bot_img = pygame.transform.scale(bot_img_old, (90, 90))
bot_img_opp = pygame.transform.rotate(bot_img, 180)
bot_img_hori_left_old = pygame.transform.rotate(bot_img_old, 90)
bot_img_hori_right_old = pygame.transform.rotate(bot_img_old, -90)
bot_img_hori_left = pygame.transform.scale(bot_img_hori_left_old, (90, 90))
bot_img_hori_right = pygame.transform.scale(bot_img_hori_right_old, (90, 90))

"""
for i in map:
    for j in i:
        print(map_elements[j])

"""


"""
for i in map:
    y = 0
    for j in i:
        screen.blit(pygame.transform.rotate(map_elements[j], angle), (y, x))
        y += 120
    x += 120
"""


def createMap():
    x = 0
    y = 0

    angle_list = 0
    angle_component = 0

    for i in map:
        angle_component = 0
        y = 0
        for j in i:
            screen.blit(pygame.transform.rotate(
                map_elements[j], angles[angle_list][angle_component]), (y, x))
            y += 120
            angle_component += 1
        x += 120
        angle_list += 1


createMap()

"""
for i in map:
    y = 0
    for j in i:
        screen.blit(pygame.transform.rotate(map_elements[j], angle), (y, x))
        y += 120
    x += 120
"""
screen.blit(bot_img, (init_x, init_y))

event = ""

pygame.display.update()

# screen.blit(pixel, ((init_x + 100), (init_y + 43)))
color = screen.get_at(((init_x + 100), (init_y + 43)))
# print(color)

while True:
    pygame.display.update()

    if init_y <= 0:
        init_y += 120
        screen.blit(bot_img, (init_x, init_y))
    if init_x <= 0:
        init_x += 120
        screen.blit(bot_img_hori_right, (init_x, init_y))
    if init_y >= 600:
        init_y -= 120
        screen.blit(bot_img, (init_x, init_y))
    if init_x >= 600:
        init_x -= 120
        screen.blit(bot_img_hori_left, (init_x, init_y))

    right_color_1 = screen.get_at(((init_x + 100), (init_y + 43)))
    left_color_1 = screen.get_at(((init_x - 14), (init_y + 43)))
    left_color_2 = screen.get_at(((init_x - 14 + 6), (init_y + 43)))
    up_color_1 = screen.get_at(((init_x + 43), (init_y - 14)))
    up_color_2 = screen.get_at(((init_x + 43 + 6), (init_y - 14 + 6)))
    down_color_1 = screen.get_at(((init_x + 43), (init_y + 100)))

    key_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event = "quit"
            pygame.quit()
            break
        elif key_pressed[pygame.K_LEFT] and left_color_1 != (237, 28, 36, 255):
            createMap()
            screen.blit(bot_img_hori_left, ((init_x - 120), (init_y)))
            init_x -= 120
        # and not init_x >= 377:
        elif key_pressed[pygame.K_RIGHT] and right_color_1 != (237, 28, 36, 255):
            createMap()
            screen.blit(bot_img_hori_right, ((init_x + 120), (init_y)))
            init_x += 120
        # and not init_y >= 377:
        elif key_pressed[pygame.K_DOWN] and down_color_1 != (237, 28, 36, 255):
            createMap()
            init_y += 120
            screen.blit(bot_img_opp, ((init_x), (init_y)))
        elif key_pressed[pygame.K_UP] and up_color_1 != (237, 28, 36, 255):
            createMap()
            screen.blit(bot_img, ((init_x), (init_y - 120)))
            init_y -= 120
        else:
            pass
    if event == "quit":
        break

    # if init_x == 497 and init_y == 497:
    #     event = "quit"
    #     pygame.quit()
    #     print("Winner winner chicken dinner")
    #     break
