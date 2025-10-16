import pygame 

pygame.init()
l = 0
my_list = [0, 1, 2, 3, 4, 4, 55, 90]
r = len(my_list)-1
target = 90
screen = pygame.display.set_mode((600, 600))
w, h = 50, 50
sx, sy = 50, 50
font = pygame.font.SysFont(None, 36)
found = False
run = True
text_target = font.render(f"Target is {target}", True, (0, 0, 0))

while run and l<r:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    for i, n in enumerate(my_list):
        x = sx + i * w
        rect = pygame.Rect((x, sy, w, h))
        pygame.draw.rect(screen, (0, 255, 0), rect)
        if i == l:
            pygame.draw.rect(screen, (0, 0, 255), rect, 3) 
        elif i == r:
            pygame.draw.rect(screen, (255, 0, 0), rect, 3)
        text = font.render(str(n), True, (0, 0, 0))
        text_center = text.get_rect(center = rect.center)
        screen.blit(text, text_center)
        screen.blit(text_target, (100, 100))
    pygame.display.update()
    pygame.time.delay(2000)
    val = my_list[l] + my_list[r]
    if val<target:
        l+=1
    elif val>target:
        r-=1
    else:
        found = True
        break
if not found:
    print("Not found")
else:
    print(f"Found at {l} and {r}")
pygame.quit()