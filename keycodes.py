key_to_usb = {
    "` ~": 53,
    "1": 30,
    "2": 31,
    "3": 32,
    "4": 33,
    "5": 34,
    "6": 35,
    "7": 36,
    "8": 37,
    "9": 38,
    "0": 39,
    "-": 45,
    "+": 46,
    "Backspace": 42,
    "Tab": 43,
    "Q": 20,
    "W": 26,
    "E": 8,
    "R": 21,
    "T": 23,
    "Y": 28,
    "U": 24,
    "I": 12,
    "O": 18,
    "P": 19,
    "[": 47,
    "]": 48,
    "|": 49,
    "CapsLock": 57,
    "A": 4,
    "S": 22,
    "D": 7,
    "F": 9,
    "G": 10,
    "H": 11,
    "J": 13,
    "K": 14,
    "L": 15,
    ":": 51,
    "\"": 52,
    "non-US-1": 50,
    "Enter": 40,
    "LShift": 225,
    "Z": 29,
    "X": 27,
    "C": 6,
    "V": 25,
    "B": 5,
    "N": 17,
    "M": 16,
    "<": 54,
    ">": 55,
    "?": 56,
    "RShift": 229,
    "LCtrl": 224,
    "LAlt": 226,
    "space": 44,
    "RAlt": 230,
    "RCtrl": 228,
    "Insert": 73,
    "Delete": 76,
    "Home": 80,
    "End": 81,
    "PgUp": 85,
    "PgDn": 86,
    "Left": 79,
    "Up": 83,
    "Down": 84,
    "Right": 89,
    "NumLock": 83,
    "Home": 95,
    "Left": 92,
    "End": 89,
    "Up": 96,
    "KP-5": 93,
    "Down": 90,
    "Ins": 98,
    "KP-*": 85,
    "PgUp": 97,
    "Right": 94,
    "PgDn": 91,
    "Del": 99,
    "KP--": 86,
    "KP-+": 87,
    "KP-Enter": 88,
    "Esc": 41,
    "F1": 58,
    "F2": 59,
    "F3": 60,
    "F4": 61,
    "F5": 62,
    "F6": 63,
    "F7": 64,
    "F8": 65,
    "F9": 66,
    "F10": 67,
    "F11": 68,
    "F12": 69,
    "PrtScr": 70,
    "Alt+SysRq": 154,
    "ScrollLock": 71,
    "Pause": 72,
    "LWin": 227,
    "RWin": 231,
}

def get_usb_code(key_name):
    return key_to_usb.get(key_name.upper(), "Key not found")

