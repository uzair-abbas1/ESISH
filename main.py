from custom_keyboard import *

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
