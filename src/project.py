import pygame 

def main():
    pygame.init

    clock = pygame.time.Clock()
    FPS = 60

# fullscreen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Cityscape")
    resolution = screen.get_size()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
# exit fullscreen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False 

#game loop
    run = True  
    while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                      run = False

if __name__ == "__main__":
    main()