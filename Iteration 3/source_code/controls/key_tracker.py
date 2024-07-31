import pygame


class KeyTracker:
    def __init__(self):
        self.keys_pressed = set()
        self._keys_just_pressed = set()

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key not in self.keys_pressed:
                self._keys_just_pressed.add(event.key)
                self.keys_pressed.add(event.key)
        elif event.type == pygame.KEYUP:
            if event.key in self.keys_pressed:
                self.keys_pressed.remove(event.key)

    def keys_just_pressed(self):
        return self._keys_just_pressed

    def is_key_just_pressed(self, key):
        return key in self._keys_just_pressed

    def is_key_pressed(self, key):
        return key in self.keys_pressed

    def clear_just_pressed(self):
        self._keys_just_pressed.clear()
