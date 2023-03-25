import keyboard
import pyautogui
from flask import Flask, request

app = Flask(__name__)

# Set the resolutions of the League of Legends on the Yuumi PC and the main PC
game_resolution = (3840, 2160)
main_pc_resolution = (5120, 2880)

# Endpoint for handling spell key presses
@app.route('/spell', methods=['POST'])
def handle_spell():
    global game_resolution

    # Get the spell action from the request
    spell_action = request.json['action']

    # Press the corresponding spell key on the keyboard
    if spell_action == 'q':
        keyboard.press('q')
    elif spell_action == 'w':
        keyboard.press('w')
    elif spell_action == 'e':
        keyboard.press('e')
    elif spell_action == 'r':
        keyboard.press('r')
    elif spell_action == 'd':
        keyboard.press('d')
    elif spell_action == 'f':
        keyboard.press('f')
    else:
        return {'error': 'Invalid spell action'}, 400

    return {'success': True}

# Endpoint for handling mouse clicks
@app.route('/click', methods=['POST'])
def handle_click():
    global game_resolution, main_pc_resolution

    # Get the mouse coordinates from the request
    mouse_x = request.json['mouse_x']
    mouse_y = request.json['mouse_y']

    # Convert the mouse coordinates from main PC screen resolution to League of Legends game resolution
    game_x = int((mouse_x / main_pc_resolution[0]) * game_resolution[0])
    game_y = int((mouse_y / main_pc_resolution[1]) * game_resolution[1])

    # Move the mouse to the specified position and click
    pyautogui.moveTo(game_x, game_y)
    pyautogui.click()

    return {'success': True}

# Endpoint for checking server connection
@app.route('/connect', methods=['GET'])
def handle_connect():
    return {'success': True}

# Start the server connection
if __name__ == '__main__':
    app.run(host='192.168.0.4', port=8000, threaded=True)
