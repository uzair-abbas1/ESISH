from pynput import keyboard

# Complete custom alphabet mapping for lowercase letters
KEY_MAP = {
    'a': '𐌀', 'b': '𐌁', 'c': '𐌂', 'd': '𐌃', 'e': '𐌄',
    'f': '𐌅', 'g': '𐌆', 'h': '𐌇', 'i': '𐌈', 'j': '𐌉',
    'k': '𐌊', 'l': '𐌋', 'm': '𐌌', 'n': '𐌍', 'o': '𐌏',
    'p': '𐌐', 'q': '𐌒', 'r': '𐌓', 's': '𐌔', 't': '𐌕',
    'u': '𐌖', 'v': '𐌗', 'w': '𐌘', 'x': '𐌙', 'y': '𐌚',
    'z': '𐌛'
}

output = []

def on_press(key):
    try:
        if key == keyboard.Key.enter:
            print("\nExiting...")
            listener.stop()  # Proper way to stop without returning False
            return

        char = key.char
        if char in KEY_MAP:
            output.append(KEY_MAP[char])
        else:
            output.append(char)

        print(''.join(output), end='\r')

    except AttributeError:
        # Ignore other special keys
        pass

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
