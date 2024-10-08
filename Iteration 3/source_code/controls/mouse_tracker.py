import pygame


class MouseTracker:
    def __init__(self):
        self.previous_state = None
        self.current_state = None

    def update(self):
        if self.previous_state is None:
            self.previous_state = pygame.mouse.get_pressed()
            self.current_state = self.previous_state
        else:
            self.previous_state = self.current_state
            self.current_state = pygame.mouse.get_pressed()

    def get_pressed(self, button=0):
        if self.current_state is None:
            self.update()
        return self.current_state[button]

    def get_just_pressed(self, button=0):
        if self.current_state is None or self.previous_state is None:
            self.update()
        return self.current_state[button] and not self.previous_state[button]

    def get_just_released(self, button=0):
        if self.current_state is None or self.previous_state is None:
            self.update()
        return not self.current_state[button] and self.previous_state[button]


mouse_tracker = MouseTracker()
