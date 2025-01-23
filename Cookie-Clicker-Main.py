import time,threading
from pynput.mouse import Controller,Button
from pynput.keyboard import Listener,KeyCode,Key


def clicker():
    while not end_script:
        if clicking:
            mouse.click(Button.left,1)
        time.sleep(0.001)

def toggle_event(key):
    if key == activation_key:
        global clicking
        clicking = not clicking
    elif key == Key.esc:
        global end_script
        end_script = True
        return False

activation_key = KeyCode(char="`")
clicking = False
end_script = False
mouse = Controller()

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_release=toggle_event) as listener:
    listener.join()