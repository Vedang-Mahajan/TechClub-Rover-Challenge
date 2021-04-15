import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Arena")

# map = [[4, 4, 4, 4, 4], [4, 4, 4, 4, 4], [4, 4, 4, 4, 4], [4, 4, 4, 4, 4], [4, 4, 4, 4, 4]]

bot_img_old = pygame.image.load("Bot Icon.png")
# arena_old = pygame.image.load("Arena.png")

left_and_right = pygame.image.load("5.png")

bot_img = pygame.transform.scale(bot_img_old, (90, 90))
# arena_img = pygame.transform.scale(arena_old, (600, 600))

# screen.blit(arena_img, (0, 0))

# for number in map:
#    for i in map[number]:
#        screen.blit(left_and_right, (120*(i+1)))

for j in range(0, 600, 120):
    for i in range(0, 600, 120):
        screen.blit(left_and_right, (i, j))
        
screen.blit(bot_img, (17, 17))

event = ""

while True:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            event = "quit"
            pygame.quit()
            break
    if event == "quit":
        break
