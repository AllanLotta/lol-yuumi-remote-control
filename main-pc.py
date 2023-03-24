import requests
import keyboard
import pyautogui

# IP address of the Yuumi PC running the Flask server
yuumi_pc_ip = '192.168.1.100'

# Port number the Flask server is running on
server_port = '8000'

# URL for the spell action endpoint
spell_url = f'http://{yuumi_pc_ip}:{server_port}/spell'

# URL for the click action endpoint
click_url = f'http://{yuumi_pc_ip}:{server_port}/click'

# Define the hotkeys
ALT_KEY = 'alt'
Q_KEY = 'q'
W_KEY = 'w'
E_KEY = 'e'
R_KEY = 'r'
D_KEY = 'd'
F_KEY = 'f'

# Define the spells corresponding to the hotkeys
SPELLS = {
    Q_KEY: 'Q',
    W_KEY: 'W',
    E_KEY: 'E',
    R_KEY: 'R',
}

# Function to send a spell action to the Yuumi PC
def cast_spell(spell_key):
    # Define the spell action as a JSON object
    spell_data = {'action': spell_key}

    # Send the spell action to the Flask server on the Yuumi PC
    response = requests.post(spell_url, json=spell_data)

    # Check if the request was successful
    if response.status_code == 200:
        print(f'Successfully cast {spell_key} spell')
    else:
        print('Failed to cast spell')

# Function to send a mouse click action to the Yuumi PC
def move_yuumi(mouse_x, mouse_y):
    # Define the mouse click action as a JSON object
    click_data = {'mouse_x': mouse_x, 'mouse_y': mouse_y}

    # Send the mouse click action to the Flask server on the Yuumi PC
    response = requests.post(click_url, json=click_data)

    # Check if the request was successful
    if response.status_code == 200:
        print(f'Successfully moved Yuumi to ({mouse_x}, {mouse_y})')
    else:
        print('Failed to move Yuumi')

# Listen for the hotkey combination to be pressed
while True:
    if keyboard.is_pressed(ALT_KEY):
        # Check if the hotkey combination is pressed
        if all([keyboard.is_pressed(key) for key in [Q_KEY, W_KEY, E_KEY, R_KEY, D_KEY, F_KEY]]):
            # Send the spell action corresponding to the first key in the combination
            spell_key = SPELLS.get(Q_KEY)
            if spell_key:
                cast_spell(spell_key)

        # Get the current mouse position
        mouse_pos = pyautogui.position()

        # Send the mouse position to the Yuumi PC to move Yuumi
        move_yuumi(mouse_pos[0], mouse_pos[1])

        # Wait for the ALT key to be released before continuing to listen
        while keyboard.is_pressed(ALT_KEY):
            pass
