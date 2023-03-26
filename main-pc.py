import sys
import requests
import threading
from pynput import mouse, keyboard
import time

running = True

yuumi_pc_ip = '192.168.0.4'
server_port = '8000'
click_url = f'http://{yuumi_pc_ip}:{server_port}/click'
spell_url = f'http://{yuumi_pc_ip}:{server_port}/spell'
level_url = f'http://{yuumi_pc_ip}:{server_port}/level'

ALT_KEY = keyboard.Key.alt_l
alt_pressed = False

action_delay = 0.5
last_action_time = 0

try:
    print('Trying to connect...')
    requests.get(f'http://{yuumi_pc_ip}:{server_port}')
    print('Connected to Yuumi PC')
except requests.exceptions.ConnectionError:
    print('\033[91m' + 'Failed to connect to Yuumi PC. Please check the server IP and try running the script again.' + '\033[0m')
    sys.exit()

def send_request(url, json_data):
    try:
        requests.post(url, json=json_data, timeout=5.0)
    except requests.exceptions.Timeout:
        print("Request timed out")

def on_key_press(key):
    global running

    # Handle key presses for abilities and summoner spells
    if alt_pressed and hasattr(key, 'char') and key.char in ['q', 'w', 'e', 'r', 'd', 'f', 'o', 'p', 'b', 'y']:
        print(f'{key.char} key pressed')
        # Define the spell action as a JSON object
        spell_data = {'action': key.char}

        # Send the spell action to the Flask server on the Yuumi PC
        try:
            requests.post(spell_url, json=spell_data, timeout=0.5)
        except requests.exceptions.Timeout:
            print('Request timed out')

        return True  # Suppress the key event

    return False

def on_hotkey_press(key):
    global alt_pressed
    if key == ALT_KEY:
        alt_pressed = True
        print('ALT key pressed')

def on_hotkey_release(key):
    global alt_pressed
    if key == ALT_KEY:
        alt_pressed = False
        print('ALT key released')

def on_click(x, y, button, pressed):
    global last_action_time, action_delay, last_action

    if alt_pressed and not pressed:
        current_time = time.time()
        if current_time - last_action_time >= action_delay:
            print(f'{button.name} button clicked at ({x}, {y})')
            click_data = {'mouse_x': x, 'mouse_y': y, 'button': button.name}
            
            # Create and start a new thread for sending the request
            request_thread = threading.Thread(target=send_request, args=(click_url, click_data))
            request_thread.start()

            last_action_time = current_time
            last_action = None

mouse_listener = mouse.Listener(on_click=on_click, daemon=True)
mouse_listener.start()

hotkey_listener = keyboard.Listener(on_press=on_hotkey_press, on_release=on_hotkey_release, daemon=True)
hotkey_listener.start()

keyboard_listener = keyboard.Listener(on_press=on_key_press, suppress=on_key_press, daemon=True)
keyboard_listener.start()

while running:
    time.sleep(1)
