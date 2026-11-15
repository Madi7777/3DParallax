import pygame 

def main():
    pygame.init

    clock = pygame.time.Clock()
    FPS = 60

    # fullscreen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
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

if __name__ == "__main__":
    main()