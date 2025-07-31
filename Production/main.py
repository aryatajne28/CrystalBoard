import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB
from kmk.extensions.rgb import AnimationModes

keyboard = KMKKeyboard()

# — Modules & Extensions —
macros = Macros()
keyboard.modules.append(macros)
keyboard.modules.append(MouseKeys())
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

# RGB: adjust pixel_pin & num_pixels if yours differ
rgb = RGB(
    pixel_pin=board.D22,
    num_pixels=87,
    animation_speed=1,
    animation_mode=AnimationModes.STATIC,
    val_default=30,
    val_limit=40
)
keyboard.extensions.append(rgb)

# — Matrix pinout (15 cols × 6 rows) —
keyboard.col_pins = (
    board.D0,  board.D1,  board.D2,  board.D3,  board.D6,
    board.D7,  board.D8,  board.D9,  board.D10, board.D11,
    board.D12, board.D13, board.D14, board.D15, board.D16
)
keyboard.row_pins = (
    board.D18, board.D19, board.D20,
    board.D21, board.D26, board.D27
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.ESC,  KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9, 
        KC.F10, KC.F11, KC.F12, KC.BSPC, KC.HOME,
        
        KC.GRV, KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5,  KC.N6,  KC.N7,  KC.N8,  KC.N9, 
        KC.N0,  KC.MINS,KC.EQL, KC.BSLS, KC.PGUP,
        
        KC.TAB, KC.Q,   KC.W,   KC.E,   KC.R,   KC.T,   KC.Y,   KC.U,   KC.I,   KC.O, 
        KC.P,   KC.LBRC,KC.RBRC,KC.ENT, KC.PGDN,
        
        KC.CAPS,KC.A,   KC.S,   KC.D,   KC.F,   KC.G,   KC.H,   KC.J,   KC.K,   KC.L, 
        KC.SCLN,KC.QUOT,KC.NO,  KC.NO,  KC.END,
        
        KC.LSFT,KC.Z,   KC.X,   KC.C,   KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM,KC.DOT, 
        KC.SLSH,KC.NO,  KC.NO,  KC.RSFT,KC.UP,
        
        KC.LCTRL,KC.LGUI,KC.LALT,KC.SPC, KC.RALT,KC.RGUI,KC.RCTL,KC.LEFT,KC.DOWN,KC.RIGHT
    ],
    
    # Fn layer
    [
        KC.ESC , KC.F1  , KC.F2  , KC.F3  , KC.F4  , KC.F5  , KC.F6  , KC.F7  , KC.F8  , KC.F9  , KC.F10 , KC.F11 , KC.F12 , KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ]
]

if __name__ == '__main__':
    keyboard.go()
