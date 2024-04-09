import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    rect_start = None
    rect_end = None
    circle_center = None
    circle_radius = 0
    eraser_radius = 20
    eraser_mode = False
    color_selection_mode = False
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_x:
                    mode = 'rectangle'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_e:
                    eraser_mode = not eraser_mode
                elif event.key == pygame.K_s:
                    color_selection_mode = not color_selection_mode
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    if mode != 'rectangle' and mode != 'circle' and not color_selection_mode:
                        radius = min(200, radius + 1)
                    elif color_selection_mode:
                        # Pick color at mouse position
                        color = screen.get_at(event.pos)
                        mode = color
                    elif mode == 'rectangle':
                        rect_start = event.pos
                    elif mode == 'circle':
                        circle_center = event.pos
                elif event.button == 3: # right click shrinks radius
                    if mode != 'rectangle' and mode != 'circle' and not color_selection_mode:
                        radius = max(1, radius - 1)
                    elif mode == 'rectangle':
                        rect_end = event.pos
                    elif mode == 'circle':
                        circle_radius = max(1, circle_radius - 1)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if mode == 'rectangle' and rect_start is not None:
                    rect_end = event.pos
                    pygame.draw.rect(screen, (255, 255, 255), (rect_start, (rect_end[0] - rect_start[0], rect_end[1] - rect_start[1])), 2)
                    rect_start = None
                    rect_end = None
                elif mode == 'circle' and circle_center is not None:
                    circle_radius = max(1, circle_radius)
                    pygame.draw.circle(screen, (255, 255, 255), circle_center, circle_radius, 2)
                    circle_center = None
                    circle_radius = 0
                    
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if not eraser_mode:
                    points.append(position)
                    points = points[-256:]
                else:
                    # Erase points within the eraser radius
                    for i in range(-eraser_radius, eraser_radius + 1):
                        for j in range(-eraser_radius, eraser_radius + 1):
                            if position[0] + i >= 0 and position[0] + i < 640 and position[1] + j >= 0 and position[1] + j < 480:
                                screen.set_at((position[0] + i, position[1] + j), (0, 0, 0))
                
        screen.fill((0, 0, 0))
        
        for i in range(len(points) - 1):
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
        
        if rect_start is not None and rect_end is not None:
            pygame.draw.rect(screen, (255, 255, 255), (rect_start, (rect_end[0] - rect_start[0], rect_end[1] - rect_start[1])), 2)
        
        if circle_center is not None:
            pygame.draw.circle(screen, (255, 255, 255), circle_center, circle_radius, 2)
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    else:
        try:
            color = pygame.Color(color_mode)
        except ValueError:
            color = (255, 255, 255)  # Default to white if color name is invalid
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()