import pygame


class KeyTracker:
    # Alphanumeric keys
    K_a = pygame.K_a
    K_b = pygame.K_b
    K_c = pygame.K_c
    K_d = pygame.K_d
    K_e = pygame.K_e
    K_f = pygame.K_f
    K_g = pygame.K_g
    K_h = pygame.K_h
    K_i = pygame.K_i
    K_j = pygame.K_j
    K_k = pygame.K_k
    K_l = pygame.K_l
    K_m = pygame.K_m
    K_n = pygame.K_n
    K_o = pygame.K_o
    K_p = pygame.K_p
    K_q = pygame.K_q
    K_r = pygame.K_r
    K_s = pygame.K_s
    K_t = pygame.K_t
    K_u = pygame.K_u
    K_v = pygame.K_v
    K_w = pygame.K_w
    K_x = pygame.K_x
    K_y = pygame.K_y
    K_z = pygame.K_z

    # Number keys
    K_0 = pygame.K_0
    K_1 = pygame.K_1
    K_2 = pygame.K_2
    K_3 = pygame.K_3
    K_4 = pygame.K_4
    K_5 = pygame.K_5
    K_6 = pygame.K_6
    K_7 = pygame.K_7
    K_8 = pygame.K_8
    K_9 = pygame.K_9

    # Special keys
    K_SPACE = pygame.K_SPACE
    K_RETURN = pygame.K_RETURN
    K_ESCAPE = pygame.K_ESCAPE
    K_BACKSPACE = pygame.K_BACKSPACE
    K_TAB = pygame.K_TAB
    K_CAPSLOCK = pygame.K_CAPSLOCK

    # Arrow keys
    K_UP = pygame.K_UP
    K_DOWN = pygame.K_DOWN
    K_LEFT = pygame.K_LEFT
    K_RIGHT = pygame.K_RIGHT

    # Function keys
    K_F1 = pygame.K_F1
    K_F2 = pygame.K_F2
    K_F3 = pygame.K_F3
    K_F4 = pygame.K_F4
    K_F5 = pygame.K_F5
    K_F6 = pygame.K_F6
    K_F7 = pygame.K_F7
    K_F8 = pygame.K_F8
    K_F9 = pygame.K_F9
    K_F10 = pygame.K_F10
    K_F11 = pygame.K_F11
    K_F12 = pygame.K_F12

    # Keypad keys
    K_KP0 = pygame.K_KP0
    K_KP1 = pygame.K_KP1
    K_KP2 = pygame.K_KP2
    K_KP3 = pygame.K_KP3
    K_KP4 = pygame.K_KP4
    K_KP5 = pygame.K_KP5
    K_KP6 = pygame.K_KP6
    K_KP7 = pygame.K_KP7
    K_KP8 = pygame.K_KP8
    K_KP9 = pygame.K_KP9
    K_KP_ENTER = pygame.K_KP_ENTER
    K_KP_PLUS = pygame.K_KP_PLUS
    K_KP_MINUS = pygame.K_KP_MINUS
    K_KP_MULTIPLY = pygame.K_KP_MULTIPLY
    K_KP_DIVIDE = pygame.K_KP_DIVIDE
    K_KP_PERIOD = pygame.K_KP_PERIOD

    # Other common keys
    K_LCTRL = pygame.K_LCTRL
    K_RCTRL = pygame.K_RCTRL
    K_LSHIFT = pygame.K_LSHIFT
    K_RSHIFT = pygame.K_RSHIFT
    K_LALT = pygame.K_LALT
    K_RALT = pygame.K_RALT
    K_HOME = pygame.K_HOME
    K_END = pygame.K_END
    K_PAGEUP = pygame.K_PAGEUP
    K_PAGEDOWN = pygame.K_PAGEDOWN
    K_INSERT = pygame.K_INSERT
    K_DELETE = pygame.K_DELETE

    def __init__(self):
        self.keys_pressed = set()
        self._keys_just_pressed = set()  # Renamed to _keys_just_pressed

    def update(self):
        self._keys_just_pressed.clear()
        for event in pygame.event.get(pygame.KEYDOWN):
            if event.key not in self.keys_pressed:
                self._keys_just_pressed.add(event.key)
                self.keys_pressed.add(event.key)

        for event in pygame.event.get(pygame.KEYUP):
            self.keys_pressed.discard(event.key)

    def keys_just_pressed(self):
        return self._keys_just_pressed
