import pygame 

pygame.init()
l = 0
my_list = [i for i in range(10)]
r = 0
max_sum = 0
cur = 0
screen = pygame.display.set_mode((600, 600))
w, h = 50, 50
sx, sy = 50, 50
font = pygame.font.SysFont(None, 36)
found = False
run = True
window = set()

while run and r<len(my_list):
    screen.fill((255, 255, 255))
    window.add(r)
    cur += my_list[r]
    max_sum = max(cur, max_sum)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            
    for i, n in enumerate(my_list):
        x = sx + i * w
        rect = pygame.Rect((x, sy, w, h))
        
        if i in window:
            pygame.draw.rect(screen, (0, 0, 255), rect) 
        else:
            pygame.draw.rect(screen, (0, 255, 0), rect)
            
        text = font.render(str(n), True, (0, 0, 0))
        text_sum = font.render(f"Current Max Triplet Sum is {max_sum}", True, (0, 0, 0))
        text_center = text.get_rect(center = rect.center)
        screen.blit(text, text_center)
        screen.blit(text_sum, (100, 100))
        
    pygame.display.update()
    pygame.time.delay(2000)
    
    r+=1
    while r-l+1>3:
        cur -= my_list[l]
        window.remove(l)
        l+=1
    

pygame.quit()