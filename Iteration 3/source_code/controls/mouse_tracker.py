import pygame


class MouseTracker:
    def __init__(self):
        self.prev_mouse_state = [0, 0, 0]
        self.current_mouse_state = [0, 0, 0]
        self._mouse_just_pressed = [0, 0, 0]
        self._mouse_just_released = [0, 0, 0]

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.current_mouse_state[event.button - 1] = 1
            self._mouse_just_pressed[event.button - 1] = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            self.current_mouse_state[event.button - 1] = 0
            self._mouse_just_released[event.button - 1] = 1

    def clear_just_events(self):
        self._mouse_just_pressed = [0, 0, 0]
        self._mouse_just_released = [0, 0, 0]

    def get_just_pressed(self):
        return self._mouse_just_pressed

    def get_just_released(self):
        return self._mouse_just_released
