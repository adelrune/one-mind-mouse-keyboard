from enum import Enum

class interception_key_state(Enum):
    INTERCEPTION_KEY_DOWN = 0x00
    INTERCEPTION_KEY_UP = 0x01
    INTERCEPTION_KEY_E0 = 0x02
    INTERCEPTION_KEY_E1 = 0x04
    INTERCEPTION_KEY_TERMSRV_SET_LED = 0x08
    INTERCEPTION_KEY_TERMSRV_SHADOW = 0x10
    INTERCEPTION_KEY_TERMSRV_VKPACKET = 0x20

class interception_filter_key_state(Enum):
    INTERCEPTION_FILTER_KEY_NONE = 0x0000
    INTERCEPTION_FILTER_KEY_ALL = 0xFFFF
    INTERCEPTION_FILTER_KEY_DOWN = interception_key_state.INTERCEPTION_KEY_UP.value
    INTERCEPTION_FILTER_KEY_UP = interception_key_state.INTERCEPTION_KEY_UP.value << 1
    INTERCEPTION_FILTER_KEY_E0 = interception_key_state.INTERCEPTION_KEY_E0.value << 1
    INTERCEPTION_FILTER_KEY_E1 = interception_key_state.INTERCEPTION_KEY_E1.value << 1
    INTERCEPTION_FILTER_KEY_TERMSRV_SET_LED = interception_key_state.INTERCEPTION_KEY_TERMSRV_SET_LED.value << 1
    INTERCEPTION_FILTER_KEY_TERMSRV_SHADOW = interception_key_state.INTERCEPTION_KEY_TERMSRV_SHADOW.value << 1
    INTERCEPTION_FILTER_KEY_TERMSRV_VKPACKET = interception_key_state.INTERCEPTION_KEY_TERMSRV_VKPACKET.value << 1

class interception_mouse_state (Enum):
    INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN = 0x001
    INTERCEPTION_MOUSE_LEFT_BUTTON_UP = 0x002
    INTERCEPTION_MOUSE_RIGHT_BUTTON_DOWN = 0x004
    INTERCEPTION_MOUSE_RIGHT_BUTTON_UP = 0x008
    INTERCEPTION_MOUSE_MIDDLE_BUTTON_DOWN = 0x010
    INTERCEPTION_MOUSE_MIDDLE_BUTTON_UP = 0x020

    INTERCEPTION_MOUSE_BUTTON_1_DOWN = INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN
    INTERCEPTION_MOUSE_BUTTON_1_UP = INTERCEPTION_MOUSE_LEFT_BUTTON_UP
    INTERCEPTION_MOUSE_BUTTON_2_DOWN = INTERCEPTION_MOUSE_RIGHT_BUTTON_DOWN
    INTERCEPTION_MOUSE_BUTTON_2_UP = INTERCEPTION_MOUSE_RIGHT_BUTTON_UP
    INTERCEPTION_MOUSE_BUTTON_3_DOWN = INTERCEPTION_MOUSE_MIDDLE_BUTTON_DOWN
    INTERCEPTION_MOUSE_BUTTON_3_UP = INTERCEPTION_MOUSE_MIDDLE_BUTTON_UP

    INTERCEPTION_MOUSE_BUTTON_4_DOWN = 0x040
    INTERCEPTION_MOUSE_BUTTON_4_UP = 0x080
    INTERCEPTION_MOUSE_BUTTON_5_DOWN = 0x100
    INTERCEPTION_MOUSE_BUTTON_5_UP = 0x200

    INTERCEPTION_MOUSE_WHEEL = 0x400
    INTERCEPTION_MOUSE_HWHEEL = 0x800

class interception_filter_mouse_state(Enum):
    INTERCEPTION_FILTER_MOUSE_NONE = 0x0000
    INTERCEPTION_FILTER_MOUSE_ALL = 0xFFFF

    INTERCEPTION_FILTER_MOUSE_LEFT_BUTTON_DOWN = interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN.value
    INTERCEPTION_FILTER_MOUSE_LEFT_BUTTON_UP = interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_UP.value
    INTERCEPTION_FILTER_MOUSE_RIGHT_BUTTON_DOWN = interception_mouse_state.INTERCEPTION_MOUSE_RIGHT_BUTTON_DOWN.value
    INTERCEPTION_FILTER_MOUSE_RIGHT_BUTTON_UP = interception_mouse_state.INTERCEPTION_MOUSE_RIGHT_BUTTON_UP.value
    INTERCEPTION_FILTER_MOUSE_MIDDLE_BUTTON_DOWN = interception_mouse_state.INTERCEPTION_MOUSE_MIDDLE_BUTTON_DOWN.value
    INTERCEPTION_FILTER_MOUSE_MIDDLE_BUTTON_UP = interception_mouse_state.INTERCEPTION_MOUSE_MIDDLE_BUTTON_UP.value

    INTERCEPTION_FILTER_MOUSE_BUTTON_1_DOWN = interception_mouse_state.INTERCEPTION_MOUSE_BUTTON_1_DOWN.value
    INTERCEPTION_FILTER_MOUSE_BUTTON_1_UP = interception_mouse_state.INTERCEPTION_MOUSE_BUTTON_1_UP.value
    INTERCEPTION_FILTER_MOUSE_BUTTON_2_DOWN = interception_mouse_state.INTERCEPTION_MOUSE_BUTTON_2_DOWN.value
    INTERCEPTION_FILTER_MOUSE_BUTTON_2_UP = interception_mouse_state.INTERCEPTION_MOUSE_BUTTON_2_UP.value
    INTERCEPTION_FILTER_MOUSE_BUTTON_3_DOWN = interception_mouse_state.INTERCEPTION_MOUSE_BUTTON_3_DOWN.value
    INTERCEPTION_FILTER_MOUSE_BUTTON_3_UP = interception_mouse_state.INTERCEPTION_MOUSE_BUTTON_3_UP.value

    INTERCEPTION_FILTER_MOUSE_BUTTON_4_DOWN = interception_mouse_state.INTERCEPTION_MOUSE_BUTTON_4_DOWN.value
    INTERCEPTION_FILTER_MOUSE_BUTTON_4_UP = interception_mouse_state.INTERCEPTION_MOUSE_BUTTON_4_UP.value
    INTERCEPTION_FILTER_MOUSE_BUTTON_5_DOWN = interception_mouse_state.INTERCEPTION_MOUSE_BUTTON_5_DOWN.value
    INTERCEPTION_FILTER_MOUSE_BUTTON_5_UP = interception_mouse_state.INTERCEPTION_MOUSE_BUTTON_5_UP.value

    INTERCEPTION_FILTER_MOUSE_WHEEL = interception_mouse_state.INTERCEPTION_MOUSE_WHEEL.value
    INTERCEPTION_FILTER_MOUSE_HWHEEL = interception_mouse_state.INTERCEPTION_MOUSE_HWHEEL.value
    INTERCEPTION_FILTER_MOUSE_MOVE = 0x1000

class interception_mouse_flag(Enum):
    INTERCEPTION_MOUSE_MOVE_RELATIVE = 0x000
    INTERCEPTION_MOUSE_MOVE_ABSOLUTE = 0x001
    INTERCEPTION_MOUSE_VIRTUAL_DESKTOP = 0x002
    INTERCEPTION_MOUSE_ATTRIBUTES_CHANGED = 0x004
    INTERCEPTION_MOUSE_MOVE_NOCOALESCE = 0x008
    INTERCEPTION_MOUSE_TERMSRV_SRC_SHADOW = 0x100