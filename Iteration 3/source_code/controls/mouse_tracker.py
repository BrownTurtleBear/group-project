import pygame


class MouseTracker:
    def __init__(self):
        self.prev_mouse_state = [0, 0, 0]
        self.current_mouse_state = [0, 0, 0]

    def update_mouse_states(self):
        self.prev_mouse_state = self.current_mouse_state[:]
        self.current_mouse_state = pygame.mouse.get_pressed()

    def get_just_pressed(self):
        just_pressed = [0, 0, 0]
        for i in range(3):
            if self.current_mouse_state[i] == 1 and self.prev_mouse_state[i] == 0:
                just_pressed[i] = 1
        return just_pressed

    def get_just_released(self):
        just_released = [0, 0, 0]
        for i in range(3):
            if self.current_mouse_state[i] == 0 and self.prev_mouse_state[i] == 1:
                just_released[i] = 1
        return just_released
